from .pkg_data.crypto import base64_to_a32, base64_url_decode, decrypt_attr, decrypt_key, a32_to_str, AES, get_chunks, str_to_a32, a32_to_base64
from tenacity import retry, wait_exponential, retry_if_exception_type, stop_after_attempt
from omnitools import def_template, randstr
from .pkg_data.mega import Counter, logger, base64_url_encode
from .pkg_data.errors import RequestError
from .pkg_data import Mega as _Mega
from pathlib import Path
import threadwrapper
import threading
import traceback
import tempfile
import requests
import secrets
import random
import shutil
import time
import copy
import json
import re
import os
# from typing import *


def mRandomToken(prefix: str):
    return "{}!{}".format(prefix, randstr(9).lower())


class Mega(_Mega):
    _local_folders = None
    blacklist_proxy = None

    def import_url(self, url: str, dest_path: str = None, dest_name: str = None):
        try:
            self.parse_folder_url(url)
        except:
            pass
        else:
            return self.import_folder(url, dest_path)
        try:
            self._parse_url(url)
        except:
            pass
        else:
            return self.import_file(url, dest_path, dest_name)
        raise Exception("cannot import url ({})".format(url))

    def import_file(self, url: str, dest_path: str = None, dest_name: str = None):
        file_handle, file_key = self._parse_url(url).split('!')
        pl_info = self.get_public_file_info(file_handle, file_key)
        if not dest_name:
            dest_name = pl_info['name']
        self.get_files()
        space = self.get_storage_space()
        space = space["total"]-space["used"]
        total_size = pl_info['size']
        if space < total_size:
            raise Exception("cannot import file ({} B total) into account ({} B remaining)".format(total_size, space))
        if not dest_path:
            dest_path = self.root_id
        else:
            dest_path = self.find_path_descriptor(dest_path)
        r = self.import_public_file(file_handle, file_key, dest_node={"h": dest_path}, dest_name=dest_name)
        self._files_cache = None
        self._local_folders = None
        return r

    def import_folder(self, url: str, dest_path: str = None):
        o_dest_path = dest_path
        self.get_files()
        space = self.get_storage_space()
        space = space["total"]-space["used"]
        files = self.get_files_in_folder(url, include_folders=True)
        total_size = sum([_["s"] for _ in files if _["t"] == 0])
        if space < total_size:
            raise Exception("cannot import folder ({} B total) into account ({} B remaining)".format(total_size, space))
        # if not dest_path:
        #     dest_path = self.root_id
        # else:
        #     dest_path = self.find_path_descriptor(dest_path)
        master_key_cipher = AES.new(a32_to_str(self.master_key), AES.MODE_ECB)
        error = None
        for file in files:
            if error:
                break
            if file["t"] == 0:
                for i in range(0, 5):
                    try:
                        k = file["key"] if file["t"] == 0 else file["k"]
                        k = base64_url_encode(master_key_cipher.encrypt(a32_to_str(k)))
                        p = self.create_folder(o_dest_path+file["path"][1:])[-1][1]
                        data = {
                            "sm": 1,
                            "v": 3,
                            "i": mRandomToken("pn"),
                            "a": "p",
                            "t": p,
                            "n": [{
                                "a": file["_a"],
                                "h": file["h"],
                                "k": k,
                                "t": file["t"],
                            }]
                        }
                        r = self._api_request(data)
                        if isinstance(r, list):
                            break
                    except:
                        if i == 4:
                            error = file
        self._files_cache = None
        self._local_folders = None
        if error:
            raise Exception("cannot import file ({}) from url ({})".format(error["path"]+error["a"]["n"], url))
        return True

    def revoke_file(self, path=None, node_id=None):
        nodes = self.get_files()
        if node_id:
            node = nodes[node_id]
        else:
            node = nodes[self.find(path)[1]["h"]]
        if not node:
            raise Exception("not find {} or {}".format(path, node_id))
        data = {
            "a": "l",
            "d": 1,
            "i": self.request_id,
            "n": node["h"],
        }
        r = self._api_request(data)
        if r != 0:
            raise Exception("invalid response", r)
        self._files_cache = None
        self._local_folders = None
        return True

    def revoke_folder(self, path=None, node_id=None):
        nodes = self.get_files()
        if node_id:
            node = nodes[node_id]
        else:
            node = nodes[self.find_path_descriptor(path)]
        if not node:
            raise Exception("not find {} or {}".format(path, node_id))
        data = {
            "a": "s2",
            "ha": "",
            "i": self.request_id,
            "n": node["h"],
            "s": [{"u": "EXP", "r": ""}]
        }
        r = self._api_request(data)
        if not("r" in r and any(_ in [0, -9] for _ in r["r"])):
            raise Exception("invalid response", r)
        self._files_cache = None
        self._local_folders = None
        return True

    def revoke(self, path):
        ids = [self.find(path), self.find_path_descriptor(path)]
        if all(ids):
            raise Exception("cannot determine file or folder for path:", path)
        if not any(ids):
            raise Exception("cannot find path:", path)
        if ids[0]:
            return self.revoke_file(node_id=ids[0][1]["h"])
        if ids[1]:
            return self.revoke_folder(node_id=ids[1])

    def export_file(self, path=None, node_id=None):
        nodes = self.get_files()
        if node_id:
            node = nodes[node_id]
        else:
            node = self.find(path)

        if not node:
            raise Exception("cannot find {} or {}".format(path, node_id))

        node_data = self._node_data(node)
        is_file_node = node_data['t'] == 0
        if not is_file_node:
            raise Exception("use export_folder instead")
        r = self._export_file([None, node])
        self._files_cache = None
        self._local_folders = None
        return r

    def export_folder(self, path=None, node_id=None):
        nodes = self.get_files()
        if node_id:
            node = nodes[node_id]
        else:
            # p=self.create_folder(path)[-1][1]
            # self.get_files()
            p = self.find_path_descriptor(path)
            if not p:
                node = None
            else:
                node = nodes[p]

        if not node:
            raise Exception("cannot find {} or {}".format(path, node_id))

        node_data = self._node_data(node)
        is_file_node = node_data['t'] == 0
        if is_file_node:
            raise Exception("use export instead")
        if node:
            if "shared_folder_key" in node:
                # If already exported
                return self.get_folder_link(node)

        child_nodes = []
        nodes_key = [node_data['k']]
        for k, v in self.get_files().items():
            if "path" in v and v["path"].startswith(self._local_folders[node_data["h"]]):
                if v["h"] != node_data["h"]:
                    child_nodes.append(v["h"])
                    nodes_key.append(v["k"] if v["t"] == 1 else v["key"])

        master_key_cipher = AES.new(a32_to_str(self.master_key), AES.MODE_ECB)
        ha = base64_url_encode(
            master_key_cipher.encrypt(node_data['h'].encode("utf8") +
                                      node_data['h'].encode("utf8")))

        share_key = secrets.token_bytes(16)
        ok = base64_url_encode(master_key_cipher.encrypt(share_key))
        share_key_cipher = AES.new(share_key, AES.MODE_ECB)

        cr2 = []
        for i in range(len(nodes_key)-1, -1, -1):
            cr2.extend([0, i, base64_url_encode(share_key_cipher.encrypt(a32_to_str(nodes_key[i])))])

        node_id = node_data['h']
        request_body = [{
            'a': 's2',
            'n': node_id,
            's': [{
                'u': 'EXP',
                'r': 0
            }],
            'i': self.request_id,
            'ok': ok,
            'ha': ha,
            'cr': [[node_id], [node_id]+child_nodes, cr2]
        }]
        r = self._api_request(request_body)
        if not("r" in r and 0 in r["r"] and "cr" in r):
            raise Exception("invalid response", r)
        self._files_cache = None
        self._local_folders = None
        nodes = self.get_files()
        return self.get_folder_link(nodes[node_id])

    # noinspection PyMethodOverriding
    def export(self, path: str):
        ids = [self.find(path), self.find_path_descriptor(path)]
        if all(ids):
            raise Exception("cannot determine file or folder for path:", path)
        if not any(ids):
            raise Exception("cannot find path:", path)
        if ids[0]:
            return self.export_file(node_id=ids[0][1]["h"])
        if ids[1]:
            return self.export_folder(node_id=ids[1])

    def find(self, filename=None, handle=None, exclude_deleted=False, strict=True) -> tuple:
        """
        Return file object from given filename
        """
        files = self.get_files()
        if handle:
            return files[handle]
        o_fn = filename
        filename = os.path.basename(filename)
        # path = Path(filename)
        # filename = path.name
        # parent_dir_name = str(path.parent).replace("\\", "/")
        # if parent_dir_name == ".":
        #     parent_dir_name = None
        # if parent_dir_name:
        #     parent_node_id = self.find_path_descriptor(parent_dir_name,
        #                                                files=files)
        for file in (files.items()):
            try:
                if filename != o_fn:
                    if (filename and file[1]['t'] == 0
                            and file[1]['a']['n'] == filename
                            and file[1]['path'] == (os.path.dirname(o_fn)+"/").replace("//", "/")):
                        if exclude_deleted and self.trashbin_id == file[1]['p']:
                            continue
                        return file
                # if parent_dir_name:
                    # if (filename and parent_node_id and file[1]['a']
                    #         and file[1]['t'] == 0
                    #         and file[1]['a']['n'] == filename
                    #         and parent_node_id == file[1]['p']):
                    #     if (exclude_deleted and self.trashbin_id
                    #             == file[1]['p']):
                    #         continue
                    #     return file
                elif (filename and file[1]['a']
                        and file[1]['t'] == 0
                        and file[1]['a']['n'] == filename):
                    if (exclude_deleted
                            and self.trashbin_id == file[1]['p']):
                        continue
                    if strict and self.root_id != file[1]['p']:
                        continue
                    return file
            except TypeError:
                continue

    # noinspection PyMethodOverriding
    def move(self, src: str, dst: str, ignore_src: bool = False, ignore_folder_in_file: bool = False):
        src2 = self.find(src)
        dst2 = self.find(dst)
        if src2:
            if not dst2 and not self.find_path_descriptor(dst):
                nd = os.path.dirname(dst) or "/"
                if nd:
                    dst3 = self.find_path_descriptor(nd)
                    if dst3:
                        dst2 = True
            if dst2:
                # file to file
                nn = os.path.basename(dst)
                if nn:
                    try:
                        dst3 = self.find_path_descriptor(os.path.dirname(dst) or "/")
                        if dst3:
                            if src2[1]["a"]["n"] != nn:
                                self.rename(src2, nn)
                            r = super().move(src2[1]["h"], dst3)
                        else:
                            raise Exception("cannot find dst folder ({})".format(dst))
                    except Exception as e:
                        raise Exception("critical error: cannot rename and move file from {} to {}".format(src, dst), e)
                else:
                    raise Exception("cannot rename file into ({})".format(dst))
            else:
                # file to folder
                dst2 = self.find_path_descriptor(dst)
                if dst2:
                    r = super().move(src2[1]["h"], dst2)
                else:
                    raise Exception("cannot find dst folder ({})".format(dst))
        else:
            if not dst2 and not self.find_path_descriptor(dst):
                nd = os.path.dirname(dst) or "/"
                if nd:
                    dst3 = self.find_path_descriptor(nd)
                    if dst3:
                        dst2 = True
            if dst2:
                # folder to file
                if ignore_folder_in_file:
                    return 1
                raise Exception("cannot move folder ({}) into file ({})".format(src, dst))
            else:
                src2 = self.find_path_descriptor(src)
                if not src2:
                    if ignore_src:
                        return 1
                    raise Exception("cannot find src folder ({})".format(dst))
                # folder to folder
                dst2 = self.find_path_descriptor(dst)
                if not dst2:
                    raise Exception("cannot find dst folder ({})".format(dst))
                r = super().move(src2, dst2)
        self._files_cache = None
        self._local_folders = None
        return r == 0

    def download(self, file, dest_path=None, dest_filename=None):
        raise NotImplementedError

    @staticmethod
    def format_file_url(file, key):
        return "https://mega.nz/file/{}#{}".format(file, key)

    @staticmethod
    def format_folder_url(root_folder, key):
        return "https://mega.nz/folder/{}#{}".format(root_folder, key)

    @staticmethod
    def parse_folder_url(url: str) -> tuple:
        folder_url_format = [
            re.compile(r"mega.[^/]+/folder/([0-z-_]+)#([0-z-_]+)(?:/folder/([0-z-_]+))*"),
            re.compile(r"mega.[^/]+/#F!([0-z-_]+)[!#]([0-z-_]+)(?:/folder/([0-z-_]+))*")
        ]
        m = re.search(folder_url_format[0], url)
        if not m:
            m = re.search(folder_url_format[1], url)
        if not m:
            raise Exception("Not a valid URL")
        root_folder = m.group(1)
        key = m.group(2)
        # You may want to use m.group(-1)
        # to get the id of the subfolder
        return (root_folder, key)
        
    @staticmethod
    def decrypt_node_key(key_str: str, shared_key: str) -> tuple:
        encrypted_key = base64_to_a32(key_str.split(":")[1])
        return decrypt_key(encrypted_key, shared_key)

    @retry(retry=retry_if_exception_type(RuntimeError),
           wait=wait_exponential(multiplier=2, min=2, max=60))
    def get_nodes_in_folder(self, root_folder: str) -> list:
        try:
            data = [{"a": "f", "c": 1, "ca": 1, "r": 1}]
            response = requests.post(
                "{}://g.api.{}/cs".format(
                    self.schema,
                    self.domain
                ),
                params={
                    "id": self.sequence_num,
                    "n": root_folder
                },
                data=json.dumps(data)
            )
            self.sequence_num += 1
            json_resp = response.json()
            if isinstance(json_resp, int):
                print("no files in folder, probably expired")
                r = []
            else:
                r = json_resp[0]["f"]
            return r
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e)

    def _get_file_data_in_folder(self, file_id, root_folder, proxies=None, v=None):
        try:
            data = [{
                "a": "g",
                "g": 1,
                "n": file_id
            }]
            if v == 2:
                data[0].update({"v": 2})
            response = requests.post(
                "{}://g.api.{}/cs".format(
                    self.schema,
                    self.domain
                ),
                params={
                    "id": self.sequence_num,
                    "n": root_folder
                },
                data=json.dumps(data),
                timeout=self.timeout,
                proxies=proxies
            )
            self.sequence_num += 1
            r = response.json()[0]
            return r
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e)

    @retry(retry=retry_if_exception_type(RuntimeError),
           wait=wait_exponential(multiplier=2, min=2, max=60))
    def get_file_data_in_folder(self, *args, **kwargs):
        return self._get_file_data_in_folder(*args, **kwargs)

    def _get_file_data(self, file_id, is_public=True, proxies=None, v=None):
        try:
            params = {'id': self.sequence_num}
            if self.sid:
                params.update({"sid": self.sid})
            data = [{
                'a': 'g',
                'g': 1,
                ('p' if is_public else 'n'): file_id
            }]
            if v == 2:
                data[0].update({"v": 2})
            response = requests.post(
                '{}://g.api.{}/cs'.format(self.schema, self.domain),
                params=params,
                data=json.dumps(data),
                timeout=self.timeout,
                proxies=proxies
            )
            self.sequence_num += 1
            r = response.json()[0]
            return r
        except requests.exceptions.RequestException as e:
            raise RuntimeError(e)

    @retry(retry=retry_if_exception_type(RuntimeError),
           wait=wait_exponential(multiplier=2, min=2, max=60))
    def get_file_data(self, *args, **kwargs):
        return self._get_file_data(*args, **kwargs)

    def get_files_in_folder(self, url: str, verbose: bool = False, include_folders: bool = False):
        folder_paths = {}
        (root_folder, shared_enc_key) = self.parse_folder_url(url)
        shared_key = base64_to_a32(shared_enc_key)
        nodes = self.get_nodes_in_folder(root_folder)
        items = []
        for i, node in enumerate(nodes):
            if isinstance(node["k"], str) and ":" in node["k"]:
                key = self.decrypt_node_key(node["k"], shared_key)
                node["key"] = key
                if node["t"] == 0:
                    node["k"] = (key[0] ^ key[4], key[1] ^ key[5], key[2] ^ key[6], key[3] ^ key[7])
                elif node["t"] == 1:
                    node["k"] = key
                node["iv"] = key[4:6] + (0, 0)
                node["meta_mac"] = key[6:8]
            # print(node)
            if isinstance(node["a"], str):
                node["_a"] = node["a"]
                node["a"] = decrypt_attr(base64_url_decode(node["a"]), node["k"])
            file_name = node["a"]["n"].strip(" ")
            file_id = node["h"]
            if verbose:
                print("\r", i+1, len(nodes), "File" if node["t"] == 0 else "Folder", file_name, flush=True)
            if node["t"] == 0:
                node["path"] = folder_paths[node["p"]]
                items.append(node)
            elif node["t"] == 1:
                parent_node = node["p"]
                if parent_node not in folder_paths:
                    folder_paths[parent_node] = "/"
                folder_paths[file_id] = folder_paths[parent_node]+file_name+"/"
                node["path"] = folder_paths[file_id]
                if include_folders:
                    items.append(node)
        if not items:
            print("no files in folder, probably empty")
        return items

    def download_files_in_folder(self, url: str, dest_path: str = None, serial_download=True, parallel_download=False, parallel_threads=2**4, verbose: bool = True, proxies=None, stop_on_exception=False) -> list:
        proxies = proxies or [None]
        items = self.get_files_in_folder(url)
        if not dest_path:
            dest_path = ""
        else:
            dest_path += "/"
        output_paths = []
        for i, item in enumerate(items):
            output_paths.append(self.download_file_in_folder(url, items[i], len(items), dest_path, i, serial_download, parallel_download, parallel_threads, verbose, proxies, stop_on_exception))
        return output_paths

    def download_file_in_folder(self, url: str, item: dict, l: int, dest_path: str = None, sequence: int = 0, serial_download=True, parallel_download=False, parallel_threads=2**4, verbose: bool = True, proxies=None, stop_on_exception=False) -> str:
        proxies = proxies or [None]
        if serial_download or parallel_download:
            if verbose:
                print("\r", sequence+1, l, item["path"], item["a"]["n"], item["s"], flush=True)
        if parallel_download:
            return self.parallel_download(item, url, dest_path+item["path"][1 if dest_path[-1] in ["\\", "//"] else 0:], None, parallel_threads, verbose, proxies, stop_on_exception)
        elif serial_download:
            return self.serial_download(item, url, dest_path+item["path"][1 if dest_path[-1] in ["\\", "//"] else 0:], None, verbose, proxies)
        raise Exception("please specify a download method: serial_download or parallel_download")

    def parallel_download(self, file_id, root_link, dest_path: str, dest_filename: str = None, parallel_threads=2**4, verbose=True, proxies=None, stop_on_exception=False) -> str:
        # if verbose:
        #     print(file_id, root_link, dest_path, dest_filename, parallel_threads, verbose, proxies, stop_on_exception)
        file_url = root_link
        file_handle = file_id
        is_dir = "/folder/" in file_url or "/#F!" in file_url
        is_public = False
        root_folder = None
        if is_dir:
            k = file_handle["k"]
            iv = file_handle["iv"]
            meta_mac = file_handle["meta_mac"]
            root_folder = self.parse_folder_url(file_url)[0]
            file_id = file_handle["h"]
            file_data = self.get_file_data_in_folder(file_id, root_folder)
            file_data2 = self.get_file_data_in_folder(file_id, root_folder, v=2)
        else:
            file = file_handle
            if isinstance(file, str):
                file_id = file
                _, file_key = self._parse_url(file_url).split("!")
                file_key = base64_to_a32(file_key)
                is_public = True
                k = (file_key[0] ^ file_key[4], file_key[1] ^ file_key[5],
                     file_key[2] ^ file_key[6], file_key[3] ^ file_key[7])
                iv = file_key[4:6] + (0, 0)
                meta_mac = file_key[6:8]
            else:
                file_id = file["h"]
                k = file["k"]
                iv = file["iv"]
                meta_mac = file["meta_mac"]
            file_data = self.get_file_data(file_id, is_public)
            file_data2 = self.get_file_data(file_id, is_public, v=2)
        if "g" not in file_data:
            # raise RequestError("File not accessible anymore")
            raise RequestError(-9)
        # elif isinstance(file_data2["g"], list):
        #     raise RequestError(-987)
        file_url = file_data["g"]
        file_size = file_data["s"]
        file_data["at"] = base64_url_decode(file_data["at"])
        file_data["at"] = decrypt_attr(file_data["at"], k)
        if dest_filename is not None:
            file_name = dest_filename
        else:
            file_name = file_data["at"]["n"]
        if not dest_path:
            dest_path = ""
        else:
            if dest_path[-1] not in ["\\", "/"]:
                dest_path += "/"
        if verbose:
            print(file_data, k, iv, meta_mac, file_url, file_size, dest_path, file_name)
        # return
        max_retry = 10
        proxies = proxies or [None]
        proxies = copy.deepcopy(proxies)
        random.SystemRandom().shuffle(proxies)
        parallel_threads *= 2
        if proxies[0] is not None:
            parallel_threads = min(parallel_threads, len(proxies))
        else:
            proxies = [None]*max_retry
        if verbose:
            print("using threads:", parallel_threads)
        tws = [threadwrapper.ThreadWrapper(threading.Semaphore(2**0)) for _ in range(0, parallel_threads)]
        cache = {}
        retry = {}
        result = {}
        timeout_blacklist = self.blacklist_proxy if self.blacklist_proxy is not None else []
        chunks = list(get_chunks(file_size))
        l = len(chunks)
        is_cloudraid_error = False
        done = False
        index = 0
        exploded = False
        downloaded = 0
        completed = 0
        temp_file_size = 0
        default_tempfile_dir = os.path.join(tempfile.gettempdir(), "megapy")
        temp_pieces_fp = os.path.join(default_tempfile_dir, "id", file_id)
        os.makedirs(temp_pieces_fp, exist_ok=True)
        default_tempfile_file_dir = os.path.join(default_tempfile_dir, "file")
        os.makedirs(default_tempfile_file_dir, exist_ok=True)
        resume_fp = os.path.join(default_tempfile_dir, "resume2.txt")
        if file_size < min(4*1024*1024*1024, shutil.disk_usage(default_tempfile_file_dir).free-0.1*1024*1024*1024):
            default_tempfile_dir = default_tempfile_file_dir
        if os.path.isfile(resume_fp):
            resume = open(resume_fp, "rb").read().decode()
            if os.path.isfile(resume):
                temp_file_size = os.path.getsize(resume)
                downloaded = temp_file_size
                completed = temp_file_size
        __file_size = 0
        l_c = 0
        _i = 0
        prev_downloaded = 0
        prev_completed = 0
        download_rate_mb = 0
        complete_rate_mb = 0
        prev_time = time.time()
        def progress():
            nonlocal download_rate_mb
            nonlocal complete_rate_mb
            nonlocal prev_time
            nonlocal prev_downloaded
            nonlocal prev_completed
            ctime = time.time()
            diff = ctime-prev_time
            if diff > 2:
                download_rate_mb = (downloaded-prev_downloaded)/(diff or 1)/1024/1024
                complete_rate_mb = (completed-prev_completed)/(diff or 1)/1024/1024
                prev_time = ctime
                prev_downloaded = downloaded
                prev_completed = completed
            print("\r", "handler   downloading piece {}/{} [{:.2f}%]   downloaded {:.2f}% [{:.2f} MB/s]   completed {:.2f}% [{:.2f} MB/s]".format(
                _i+1,
                l,
                (_i+1)/l*100,
                downloaded/(file_size or 1)*100,
                download_rate_mb,
                completed/(file_size or 1)*100,
                complete_rate_mb,
            ), end="", flush=True)
        def file_handler():
            nonlocal index
            nonlocal done
            nonlocal exploded
            nonlocal completed
            nonlocal __file_size
            nonlocal l_c
            prev_time = time.time()
            try:
                if temp_file_size:
                    temp_output_file = open(resume, "a+b")
                else:
                    temp_output_file = tempfile.NamedTemporaryFile(
                        mode="w+b",
                        prefix="megapy_",
                        delete=False,
                        dir=default_tempfile_dir
                    )
                k_str = a32_to_str(k)
                counter = Counter.new(128, initial_value=((iv[0] << 32) + iv[1]) << 64)
                aes = AES.new(k_str, AES.MODE_CTR, counter=counter)
                mac_str = "\0" * 16
                mac_encryptor = AES.new(k_str, AES.MODE_CBC, mac_str.encode("utf8"))
                iv_str = a32_to_str([iv[0], iv[1], iv[0], iv[1]])
                if temp_file_size:
                    if verbose:
                        print("\rresuming, fast forwarding aes counter", end="")
                    remaining = temp_file_size
                    _size = 65536
                    while remaining > 0:
                        print("\r", "resuming, fast forwarding, remaining", remaining, end="")
                        hm = min(_size, remaining)
                        aes.decrypt(b"\0"*hm)
                        remaining -= hm
                    print("\rresumed, fast forward complete", end="")
                while index < l and not exploded:
                    try:
                        _file_size, chunk = result.pop(index)
                        if _file_size is Exception:
                            raise Exception("ran out of proxies, cannot download part {} bytes {}-{}".format(chunk[0], chunk[2], chunk[3]))
                        if isinstance(chunk, str):
                            _chunk = chunk
                            chunk = open(_chunk, "rb").read()
                            os.remove(_chunk)
                        l_c = len(chunk)
                        __file_size = _file_size
                        if verbose:
                            progress()
                            # print("got chunk", index+1, "out of", l, _file_size, l_c)
                        if _file_size != l_c:
                            open(os.path.join(tempfile.gettempdir(), "megapy", "csm-{}-{}-{}-{}.bin".format(file_id, index, _file_size, int(time.time()))), "wb").write(chunk)
                            raise Exception("chunk size mismatch")
                        completed += l_c
                        chunk = aes.decrypt(chunk)
                        temp_output_file.write(chunk)
                        if not temp_file_size:
                            encryptor = AES.new(k_str, AES.MODE_CBC, iv_str)
                            for i in range(0, l_c - 16, 16):
                                block = chunk[i:i + 16]
                                encryptor.encrypt(block)
                            if _file_size > 16:
                                i += 16
                            else:
                                i = 0
                            block = chunk[i:i + 16]
                            if len(block) % 16:
                                block += b"\0" * (16 - (len(block) % 16))
                            mac_str = mac_encryptor.encrypt(encryptor.encrypt(block))
                        index += 1
                        open(resume_fp, "wb").write(temp_output_file.name.encode())
                        if verbose:
                            progress()
                            # print("completed chunks", index+1, "out of", l, completed/file_size*100)
                        prev_time = time.time()
                    except KeyError:
                        time.sleep(1/1000)
                        cur_time = time.time()
                        if cur_time-prev_time>1:
                            prev_time = cur_time
                            progress()
                            # print("handler listening chunk", index+1, "out of", l)
                    except Exception as e:
                        raise e
                if not exploded:
                    if not temp_file_size:
                        file_mac = str_to_a32(mac_str)
                        if (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3]) != meta_mac:
                            raise ValueError("Mismatched mac; file {} ({}) may be fine actually; this error may be caused by cloudraid file migration and Mega fucked up the hashing".format(dest_path+file_name, temp_output_file.name))
                    output_path = Path(dest_path + file_name)
                    output_path.parent.mkdir(parents=True, exist_ok=True)
                    temp_output_file.close()
                    if verbose:
                        print("\rmoving", temp_output_file.name, "==>", output_path)
                    shutil.move(temp_output_file.name, output_path, copy_function=shutil.copyfile)
                    os.remove(resume_fp)
                    if verbose:
                        print("\rmoved", temp_output_file.name, "==>", output_path)
            except:
                print("\rhandler")
                traceback.print_exc()
                exploded = True
            done = True
        def job(i, j, a, b):
            nonlocal _i
            nonlocal exploded
            nonlocal downloaded
            stime = time.time()
            if exploded:
                print("\r", "exploded", end="")
                return
            class _r:
                content = b""
                status_code = 404
                def close(self):
                    pass
            # open("log.log", "ab").write(("{}_{} start\n".format(proxies[j], i)).encode())
            temp_piece_fp = os.path.join(temp_pieces_fp, "{}_{}_{}.bin".format(i, a, b))
            try:
                proxy = {"all": proxies[j]} if proxies[j] else None
                if proxies[j]:
                    if proxies[j] not in timeout_blacklist:
                        try:
                            if os.path.isfile(temp_piece_fp):
                                r = _r()
                                r.status_code = 200
                                r.content = open(temp_piece_fp, "rb").read()
                                os.remove(temp_piece_fp)
                            else:
                                if j not in cache:
                                    if is_dir:
                                        cache[j] = self._get_file_data_in_folder(file_id, root_folder, proxy)["g"]+"/{}-{}"
                                    else:
                                        cache[j] = self._get_file_data(file_id, is_public, proxy)["g"]+"/{}-{}"
                                url = cache[j].format(a, b)
                                r = requests.get(url, stream=True, timeout=5, proxies=proxy)
                        except:
                            traceback.print_exc()
                            r = _r()
                            r.status_code = 500
                    else:
                        if verbose:
                            print("proxy in blacklist")
                        r = _r()
                        r.status_code = 300
                else:
                    try:
                        r = requests.get(file_url+"/{}-{}".format(a, b), stream=True, timeout=5, proxies=proxy)
                    except:
                        traceback.print_exc()
                        r = _r()
                        r.status_code = 500
                try:
                    c = r.content
                    if not c:
                        if not i and r.status_code != 509 and isinstance(file_data2["g"], list):
                            nonlocal is_cloudraid_error
                            is_cloudraid_error = True
                            raise RequestError(-987)
                        else:
                            raise
                except RequestError as e:
                    raise e
                except:
                    if verbose:
                        print("empty content")
                    status_code = r.status_code
                    r = _r()
                    if status_code != 200:
                        r.status_code = status_code
                # if time.time()-stime>10:
                #     if proxies[j]:
                #         if proxies[j] not in timeout_blacklist:
                #             timeout_blacklist.append(proxies[j])
                if r.status_code != 200:
                    if stop_on_exception and abs((j+1)%len(proxies)-retry[i]) > max_retry:
                        r.close()
                        raise Exception("stop_on_exception", stop_on_exception, r.status_code)
                    if proxies[j]:
                        if proxies[j] not in timeout_blacklist and r.status_code != 509:
                            timeout_blacklist.append(proxies[j])
                            # open("timeout_blacklist.json", "wb").write(json.dumps(timeout_blacklist).encode())
                    if (j+1)%len(proxies) != retry[i]:
                        if verbose:
                            print("\r", "failed to get chunk", i+1, "out of", l, a, b, ", trying proxy", j+1, "out of", len(proxies))
                            print("\r", proxies[j], r.status_code)
                        # open("log.log", "ab").write(("{}_{} end\n".format(proxies[j], i)).encode())
                        r.close()
                        # job(i, j+1, a, b)
                        job(i, (j+1)%len(proxies), a, b)
                        return
                    else:
                        result[i] = [Exception, [i,j,a,b]]
                        r.close()
                else:
                    _i = i
                        # print("getting chunk", i+1, "out of", l, a, b)
                    if i-index>parallel_threads*(2**3):
                        open(temp_piece_fp, "wb").write(c)
                        c = temp_piece_fp
                    result[i] = [b-a+1, c]
                    downloaded += b-a+1
                        # print("downloaded chunks", i+1, "out of", l, a, b, downloaded/file_size*100)
                    r.close()
            except:
                print("\rjob")
                traceback.print_exc()
                exploded = True
            # open("log.log", "ab").write(("{}_{} end\n".format(proxies[j], i)).encode())
        p = threading.Thread(target=file_handler)
        p.daemon = True
        p.start()
        for i, (a, b) in enumerate(chunks):
            if exploded:
                break
            if a + b <= temp_file_size:
                index = i+1
                if verbose:
                    print("\rskipped chunk", i+1, a, a+b-1, end="")
                continue
            if proxies[0]:
                while True:
                    # j = get_min_load_proxy_j()
                    if len(timeout_blacklist) == len(proxies):
                        exploded = True
                        break
                    else:
                        j = random.SystemRandom().choice(list(range(0, len(proxies))))
                    if proxies[j] in timeout_blacklist:
                        j = -1
                    if j == -1:
                        time.sleep(1/10)
                        print("\rretrying", i, j)
                    else:
                        break
            else:
                j = random.SystemRandom().choice(list(range(0, len(proxies))))
            if exploded:
                break
            # tws[j].add(job=def_template(job, i, j, a, a+b-1))
            # j = i%parallel_threads
            retry[i] = j
            tws[i%parallel_threads].add(job=def_template(job, i, j, a, a+b-1))
        [tw.wait() for tw in tws]
        while not done:
            time.sleep(1/10)
        if exploded:
            if is_cloudraid_error:
                if os.path.isfile(resume_fp):
                    os.remove(resume_fp)
                raise RequestError(-987)
            else:
                raise Exception("parallel download failed")
        else:
            os.rmdir(temp_pieces_fp)
        return dest_path + file_name

    def get_file_name(self,
                       file_handle,
                       file_key=None):
        if file_key is None and file_handle.startswith("http"):
            file_handle, file_key = self._parse_url(file_handle).split("!")
        file_key = base64_to_a32(file_key)
        file_data = self._api_request({
            'a': 'g',
            'g': 1,
            'p': file_handle
        })
        k = (file_key[0] ^ file_key[4], file_key[1] ^ file_key[5],
             file_key[2] ^ file_key[6], file_key[3] ^ file_key[7])
        if 'g' not in file_data:
            raise RequestError('File not accessible anymore')
        attribs = base64_url_decode(file_data['at'])
        attribs = decrypt_attr(attribs, k)
        file_name = attribs['n']
        return file_name

    def get_file_size(self,
                       file_handle,
                       file_key=None):
        if file_key is None and file_handle.startswith("http"):
            file_handle, file_key = self._parse_url(file_handle).split("!")
        file_data = self._api_request({
            'a': 'g',
            'g': 1,
            'p': file_handle
        })
        if 'g' not in file_data:
            raise RequestError('File not accessible anymore')
        return file_data['s']

    def get_file_link(self,
                       file_handle,
                       file_key=None):
        if file_key is None and file_handle.startswith("http"):
            file_handle, file_key = self._parse_url(file_handle).split("!")
        file_data = self._api_request({
            'a': 'g',
            'g': 1,
            'p': file_handle
        })
        if 'g' not in file_data:
            raise RequestError('File not accessible anymore')
        return file_data['g']

    def _download_file(self, file_handle=None, file_key=None, dest_path=None, dest_filename=None, is_public=False, file=None, serial_download=True, parallel_download=False, parallel_threads=2**4, verbose=True, proxies=None, stop_on_exception=False, url=None):
        proxies = proxies or [None]
        if serial_download or parallel_download:
            if verbose:
                print("\r", file_handle if is_public else file, url, dest_path, dest_filename, flush=True)
        if parallel_download:
            return self.parallel_download(file_handle if is_public else file, url, dest_path, dest_filename, parallel_threads, verbose, proxies, stop_on_exception)
        elif serial_download:
            return self.serial_download(file_handle if is_public else file, url, dest_path, dest_filename, verbose, proxies)
        raise Exception("please specify a download method: serial_download or parallel_download")

    def serial_download(self, file_handle, file_url, dest_path: str, dest_filename: str = None, verbose: bool = False, proxies=None):
        # print(file_handle, file_url, dest_path, dest_filename, verbose, proxies)
        # tbd
        # exception
        proxies = proxies or [None]
        proxy = random.SystemRandom().choice(proxies)
        proxy = random.SystemRandom().choice(proxies)
        is_dir = "/folder/" in file_url or "/#F!" in file_url
        is_public = False
        root_folder = None
        if is_dir:
            k = file_handle["k"]
            iv = file_handle["iv"]
            meta_mac = file_handle["meta_mac"]
            root_folder = self.parse_folder_url(file_url)[0]
            file_id = file_handle["h"]
            file_data = self.get_file_data_in_folder(file_id, root_folder, proxy)
            file_data2 = self.get_file_data_in_folder(file_id, root_folder, proxy, v=2)
        else:
            file = file_handle
            if isinstance(file, str):
                file_id = file
                _, file_key = self._parse_url(file_url).split("!")
                file_key = base64_to_a32(file_key)
                is_public = True
                k = (file_key[0] ^ file_key[4], file_key[1] ^ file_key[5],
                     file_key[2] ^ file_key[6], file_key[3] ^ file_key[7])
                iv = file_key[4:6] + (0, 0)
                meta_mac = file_key[6:8]
            else:
                file_id = file["h"]
                k = file["k"]
                iv = file["iv"]
                meta_mac = file["meta_mac"]
            file_data = self.get_file_data(file_id, is_public, proxy)
            file_data2 = self.get_file_data(file_id, is_public, proxy, v=2)
        if "g" not in file_data:
            # raise RequestError("File not accessible anymore")
            raise RequestError(-9)
        # elif isinstance(file_data2["g"], list):
        #     raise RequestError(-987)
        file_url = file_data["g"]
        file_size = file_data["s"]
        file_data["at"] = base64_url_decode(file_data["at"])
        file_data["at"] = decrypt_attr(file_data["at"], k)
        if dest_filename is not None:
            file_name = dest_filename
        else:
            file_name = file_data["at"]["n"]
        if not dest_path:
            dest_path = ""
        else:
            if dest_path[-1] not in ["\\", "/"]:
                dest_path += "/"
        if verbose:
            print(file_data, proxy, k, iv, meta_mac, file_url, file_size, dest_path, file_name)
        # return
        r = requests.get(file_url, stream=True, proxies={"all": proxy} if proxy else None, timeout=5)
        if r.status_code == 509:
            raise Exception("transfer quota exceeded. please try again with other IP", proxy)
        input_file = r.raw
        speed = 0
        eta = 0
        completed = 0
        temp_file_size = 0
        default_tempfile_dir = os.path.join(tempfile.gettempdir(), "megapy")
        resume_fp = os.path.join(default_tempfile_dir, "resume2.txt")
        os.makedirs(default_tempfile_dir, exist_ok=True)
        default_tempfile_file_dir = os.path.join(default_tempfile_dir, "file")
        os.makedirs(default_tempfile_file_dir, exist_ok=True)
        if file_size < min(4*1024*1024*1024, shutil.disk_usage(default_tempfile_file_dir).free-0.1*1024*1024*1024):
            default_tempfile_dir = default_tempfile_file_dir
        if os.path.isfile(resume_fp):
            resume = open(resume_fp, "rb").read().decode()
            if os.path.isfile(resume):
                temp_file_size = os.path.getsize(resume)
                completed = temp_file_size
        if temp_file_size:
            temp_output_file = open(resume, "a+b")
        else:
            temp_output_file = tempfile.NamedTemporaryFile(
                mode="w+b",
                prefix="megapy_",
                delete=False,
                dir=default_tempfile_dir
            )
        k_str = a32_to_str(k)
        counter = Counter.new(128, initial_value=((iv[0] << 32) + iv[1]) << 64)
        aes = AES.new(k_str, AES.MODE_CTR, counter=counter)
        mac_str = "\0" * 16
        mac_encryptor = AES.new(k_str, AES.MODE_CBC, mac_str.encode("utf8"))
        iv_str = a32_to_str([iv[0], iv[1], iv[0], iv[1]])
        prev_time = time.time()
        prev_completed = temp_file_size
        for index, (chunk_start, chunk_size) in enumerate(get_chunks(file_size)):
            chunk = None
            try:
                chunk = input_file.read(chunk_size)
            except Exception as e:
                if not index and not chunk and r.status_code != 509 and isinstance(file_data2["g"], list):
                    raise RequestError(-987)
                else:
                    raise e
            l_c = len(chunk)
            if chunk_size != l_c:
                open(os.path.join(tempfile.gettempdir(), "megapy", "csm-{}-{}-{}-{}.bin".format(file_id, index, chunk_size, int(time.time()))), "wb").write(chunk)
                raise Exception("chunk size mismatch")
            completed += l_c
            chunk = aes.decrypt(chunk)
            temp_output_file.write(chunk)
            if not temp_file_size:
                encryptor = AES.new(k_str, AES.MODE_CBC, iv_str)
                for i in range(0, l_c - 16, 16):
                    block = chunk[i:i + 16]
                    encryptor.encrypt(block)
                if chunk_size > 16:
                    i += 16
                else:
                    i = 0
                block = chunk[i:i + 16]
                if len(block) % 16:
                    block += b"\0" * (16 - (len(block) % 16))
                mac_str = mac_encryptor.encrypt(encryptor.encrypt(block))
            open(resume_fp, "wb").write(temp_output_file.name.encode())
            ctime = time.time()
            diff = ctime-prev_time
            if diff>2:
                speed = (completed-prev_completed)/file_size/(diff or 1)
                eta = (file_size-completed)/speed
                speed = speed/1024/1024
                prev_time = ctime
                prev_completed = completed
            print("\r", "completed: {}/{} [{:.2f}%] speed: {:.2f} MB/s eta: {}m {}s".format(
                completed,
                file_size,
                completed/file_size*100,
                speed,
                eta//60,
                eta%60
            ), end="", flush=True)
        if not temp_file_size:
            file_mac = str_to_a32(mac_str)
            if (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3]) != meta_mac:
                raise ValueError("Mismatched mac; file {} ({}) may be fine actually; this error may be caused by cloudraid file migration and Mega fucked up the hashing".format(dest_path+file_name, temp_output_file.name))
        output_path = Path(dest_path + file_name)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        temp_output_file.close()
        shutil.move(temp_output_file.name, output_path, copy_function=shutil.copyfile)
        os.remove(resume_fp)
        return dest_path + file_name

    def download_url(self, url, dest_path=None, dest_filename=None, serial_download=True, parallel_download=False, parallel_threads=2**4, verbose=True, proxies=None, stop_on_exception=False):
        proxies = proxies or [None]
        path = self._parse_url(url).split('!')
        file_id = path[0]
        file_key = path[1]
        return self._download_file(
            url=url,
            file_handle=file_id,
            file_key=file_key,
            dest_path=dest_path,
            dest_filename=dest_filename,
            is_public=True,
            file=None,
            serial_download=serial_download,
            parallel_download=parallel_download,
            parallel_threads=parallel_threads,
            verbose=verbose,
            proxies=proxies,
            stop_on_exception=stop_on_exception
        )



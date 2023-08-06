from omnitools import REQUIRE, def_template, b64e, b64d
if REQUIRE("megadownloader"):
    from megadownloader.pkg_data.crypto import a32_to_str, AES, get_chunks, str_to_a32, makebyte, base64_url_encode, encrypt_attr, a32_to_base64, encrypt_key
    from megadownloader.pkg_data.mega import Counter, logger
    from megadownloader.utils2 import Mega as _Mega
else:
    from .pkg_data.crypto import a32_to_str, AES, get_chunks, str_to_a32, makebyte, base64_url_encode, encrypt_attr, a32_to_base64, encrypt_key
    from .pkg_data.mega import Counter, logger
    from .utils2 import Mega as _Mega
from pathlib import Path
import threadwrapper
import threading
import traceback
import requests
import pickle
import random
import time
import json
import copy
import os
import re
from typing import Callable, List, Dict


class FindResult:
    def __init__(self, find_result: list):
        self.file_id = find_result[0]
        self.file_data = find_result[1]

    def __format__(self, format_spec):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "<megauploader.utils.FindResult(file_id={}, file_data={{{} ...}})>".format(
            json.dumps(self.file_id),
            json.dumps(self.file_data)[1:31]
        )


class Mega(_Mega):
    _files_cache = None
    _storage_space_cache = None

    def download(self, file, dest_path=None, dest_filename=None, serial_download=True, parallel_download=False, parallel_threads=2**4, verbose=True, proxies=None, stop_on_exception=False):
        """
        Download a file by it's file object
        """
        if isinstance(file, FindResult):
            file = file.file_data
        else:
            file = file[1]
        if "path" in file:
            if dest_path:
                dest_path += file["path"][1 if dest_path[-1] in ["\\", "/"] else 0:]
            else:
                dest_path = file["path"][1:]
        return self._download_file(
            url="",
            file_handle=None,
            file_key=None,
            dest_path=dest_path,
            dest_filename=dest_filename,
            is_public=False,
            file=file,
            serial_download=serial_download,
            parallel_download=parallel_download,
            parallel_threads=parallel_threads,
            verbose=verbose,
            proxies=proxies,
            stop_on_exception=stop_on_exception
        )

    def filter(self, regex: re.Pattern, exclude_deleted=False):
        if not isinstance(regex, re.Pattern):
            if isinstance(regex, str):
                regex = re.compile(regex)
            else:
                raise Exception("is not a regular expression", regex)
        matches = []
        files = self.get_files()
        for file in files.items():
            if (file[1]['t'] == 0
                    and file[1]['a']['n']
                    and file[1]['path']
                    and regex.search(file[1]['path']+file[1]['a']['n'])):
                if (exclude_deleted and self.trashbin_id
                        == file[1]['p']):
                    continue
                matches.append(file)
        return matches

    def findall(self, filename=None, exclude_deleted=False, strict=True) -> List[Dict[str, dict]]:
        matches = []
        files = self.get_files()
        path = Path(filename)
        filename = path.name
        parent_dir_name = str(path.parent).replace("\\", "/")
        if parent_dir_name == ".":
            parent_dir_name = None
        if parent_dir_name:
            parent_node_id = self.find_path_descriptor(parent_dir_name,
                                                       files=files)
        for file in (files.items()):
            try:
                if parent_dir_name:
                    if (filename and parent_node_id and file[1]['a']
                            and file[1]['a']['n'] == filename
                            and parent_node_id == file[1]['p']):
                        if (exclude_deleted and self.trashbin_id
                                == file[1]['p']):
                            continue
                        matches.append(file)
                elif (filename and file[1]['a']
                      and file[1]['a']['n'] == filename):
                    if (exclude_deleted
                            and self.trashbin_id == file[1]['p']):
                        continue
                    if strict and self.root_id != file[1]['p']:
                        continue
                    matches.append(file)
            except TypeError:
                continue
        return matches

    def get_files(self, exclude_deleted=False) -> Dict[str, dict]:
        logger.info('Getting all files...')
        if not self._local_folders:
            self._local_folders = {}
        if self._files_cache:
            files_dict = self._files_cache
        else:
            files = self._api_request({'a': 'f', 'c': 1, 'r': 1})
            files_dict = {}
            shared_keys = {}
            self._init_shared_keys(files, shared_keys)
            for file in files['f']:
                try:
                    file["_a"] = file["a"]
                    processed_file = self._process_file(file, shared_keys)
                    # ensure each file has a name before returning
                    if processed_file['a']:
                        parent = processed_file["p"]
                        file_id = processed_file["h"]
                        file_name = processed_file["a"]["n"]
                        if parent not in self._local_folders:
                            self._local_folders[parent] = "/"
                        if processed_file["t"] == 1:
                            self._local_folders[file_id] = self._local_folders[parent]+file_name+"/"
                            processed_file["path"] = self._local_folders[file_id]
                        elif processed_file["t"] == 0:
                            processed_file["path"] = self._local_folders[parent]
                        if processed_file['p'] == self.trashbin_id and exclude_deleted:
                            continue
                        files_dict[file['h']] = processed_file
                except:
                    import traceback
                    traceback.print_exc()
                    raise
            self._files_cache = files_dict
        return files_dict

    def create_folder(self, name, dest=None) -> List[list]:
        dirs = tuple(dir_name for dir_name in str(name).split('/') if dir_name)
        folder_node_ids = {}
        for idx, directory_name in enumerate(dirs):
            existing_node_id = self.find_path_descriptor("/".join(dirs[:idx+1]))
            if existing_node_id:
                folder_node_ids[idx] = existing_node_id
                continue
            if idx == 0:
                if dest is None:
                    parent_node_id = self._root_node_id()
                else:
                    parent_node_id = dest
            else:
                parent_node_id = folder_node_ids[idx - 1]
            created_node = self._mkdir(name=directory_name,
                                       parent_node_id=parent_node_id)
            processed_file = self._process_file(created_node["f"][0], self.shared_keys)
            file_id = processed_file["h"]
            parent = processed_file["p"]
            file_name = processed_file["a"]["n"]
            if parent not in self._local_folders:
                self._local_folders[parent] = "/"
            self._local_folders[file_id] = self._local_folders[parent]+file_name+"/"
            self._files_cache[file_id] = processed_file
            node_id = created_node['f'][0]['h']
            folder_node_ids[idx] = node_id
            # print(folder_node_ids)
        return [[i, id, dirs[i]] for i, id in folder_node_ids.items()]

    def get_items_in_folder(self, path: str, strict: bool = False) -> Dict[str, dict]:
        def loop_folder(folders):
            for folder in folders:
                n_files = {id: data for id, data in files.items() if data["p"] == folder and data["t"] == 0}
                if n_files:
                    r.update(n_files)
                n_folders = {id: data for id, data in files.items() if data["p"] == folder and data["t"] == 1}
                if n_folders:
                    loop_folder(n_folders)
        r = {}
        files = self.get_files(exclude_deleted=True)
        # folder = self.find_path_descriptor(name, files=files)
        # n_folders = {folder: {"a": {"n": name}}}
        # loop_folder(n_folders)
        for id, data in files.items():
            if data["t"] == 0 and (data["path"] == path if strict else data["path"].startswith(path)):
                r[id] = data
        return r

    def serial_upload(self, filename, dest=None, dest_filename=None) -> dict:
        # determine storage node
        if dest is None:
            # if none set, upload to cloud drive node
            if not self.root_id:#hasattr(self, 'root_id'):
                self.get_files()
            dest = self.root_id

        # request upload url, call 'u' method
        input_file = open(filename, 'rb')
        file_size = os.path.getsize(filename)
        ul_url = self._api_request({'a': 'u', 's': file_size})['p']

        # generate random aes key (128) for file
        ul_key = [random.randint(0, 0xFFFFFFFF) for _ in range(6)]
        k_str = a32_to_str(ul_key[:4])
        count = Counter.new(
            128, initial_value=((ul_key[4] << 32) + ul_key[5]) << 64)
        aes = AES.new(k_str, AES.MODE_CTR, counter=count)

        upload_progress = 0
        completion_file_handle = None

        mac_str = '\0' * 16
        mac_encryptor = AES.new(k_str, AES.MODE_CBC,
                                mac_str.encode("utf8"))
        iv_str = a32_to_str([ul_key[4], ul_key[5], ul_key[4], ul_key[5]])
        if file_size > 0:
            for chunk_start, chunk_size in get_chunks(file_size):
                chunk = input_file.read(chunk_size)
                upload_progress += len(chunk)

                encryptor = AES.new(k_str, AES.MODE_CBC, iv_str)
                for i in range(0, len(chunk) - 16, 16):
                    block = chunk[i:i + 16]
                    encryptor.encrypt(block)

                # fix for files under 16 bytes failing
                if chunk_size > 16:
                    i += 16
                else:
                    i = 0

                block = chunk[i:i + 16]
                if len(block) % 16:
                    block += makebyte('\0' * (16 - len(block) % 16))
                mac_str = mac_encryptor.encrypt(encryptor.encrypt(block))

                # encrypt file and upload
                chunk = aes.encrypt(chunk)
                output_file = requests.post(ul_url + "/" +
                                            str(chunk_start),
                                            data=chunk,
                                            timeout=self.timeout)
                completion_file_handle = output_file.text
                logger.info('%s of %s uploaded', upload_progress,
                            file_size)
        else:
            output_file = requests.post(ul_url + "/0",
                                        data='',
                                        timeout=self.timeout)
            completion_file_handle = output_file.text

        input_file.close()

        logger.info('Chunks uploaded')
        logger.info('Setting attributes to complete upload')
        logger.info('Computing attributes')
        file_mac = str_to_a32(mac_str)

        # determine meta mac
        meta_mac = (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3])

        dest_filename = dest_filename or os.path.basename(filename)
        attribs = {'n': dest_filename}

        encrypt_attribs = base64_url_encode(
            encrypt_attr(attribs, ul_key[:4]))
        key = [
            ul_key[0] ^ ul_key[4], ul_key[1] ^ ul_key[5],
            ul_key[2] ^ meta_mac[0], ul_key[3] ^ meta_mac[1], ul_key[4],
            ul_key[5], meta_mac[0], meta_mac[1]
        ]
        encrypted_key = a32_to_base64(encrypt_key(key, self.master_key))
        logger.info('Sending request to update attributes')
        # update attributes
        data = self._api_request({
            'a':
            'p',
            't':
            dest,
            'i':
            self.request_id,
            'n': [{
                'h': completion_file_handle,
                't': 0,
                'a': encrypt_attribs,
                'k': encrypted_key
            }]
        })
        logger.info('Upload complete')
        return data

    def parallel_upload(self, filename, dest=None, dest_filename=None, auto_split=None, parallel_threads=2**3, verbose: bool = True, proxies=None) -> dict:
        proxies = proxies or [None]
        proxies = copy.deepcopy(proxies)
        random.SystemRandom().shuffle(proxies)
        if proxies[0] is not None:
            parallel_threads = min(parallel_threads, len(proxies))
        else:
            proxies = [None]*10
        # determine storage node
        if dest is None:
            # if none set, upload to cloud drive node
            if not self.root_id:#hasattr(self, 'root_id'):
                self.get_files()
            dest = self.root_id

        # request upload url, call 'u' method
        input_file = open(filename, 'rb')
        file_size = os.path.getsize(filename)
        if auto_split:
            file_size = auto_split[1]-auto_split[0]
            input_file.seek(auto_split[0])
        ul_url = self._api_request({'a': 'u', 's': file_size})['p']

        # generate random aes key (128) for file
        ul_key = [random.randint(0, 0xFFFFFFFF) for _ in range(6)]
        k_str = a32_to_str(ul_key[:4])
        count = Counter.new(
            128, initial_value=((ul_key[4] << 32) + ul_key[5]) << 64)
        aes = AES.new(k_str, AES.MODE_CTR, counter=count)

        upload_progress = 0
        completion_file_handle = []

        mac_str = '\0' * 16
        mac_encryptor = AES.new(k_str, AES.MODE_CBC,
                                mac_str.encode("utf8"))
        iv_str = a32_to_str([ul_key[4], ul_key[5], ul_key[4], ul_key[5]])
        exploded = False
        if verbose:
            print(ul_url, dest, dest_filename, auto_split, filename, file_size)
        if file_size > 0:
            timeout_blacklist = []
            retry_j = {}
            tws = [threadwrapper.ThreadWrapper(threading.Semaphore(2**0)) for i in range(0, parallel_threads)]
            chunks = list(get_chunks(file_size))
            for index, (chunk_start, chunk_size) in enumerate(chunks):
                if exploded:
                    break
                chunk = input_file.read(chunk_size)
                upload_progress += len(chunk)

                encryptor = AES.new(k_str, AES.MODE_CBC, iv_str)
                for i in range(0, len(chunk) - 16, 16):
                    block = chunk[i:i + 16]
                    encryptor.encrypt(block)

                # fix for files under 16 bytes failing
                if chunk_size > 16:
                    i += 16
                else:
                    i = 0

                block = chunk[i:i + 16]
                if len(block) % 16:
                    block += makebyte('\0' * (16 - len(block) % 16))
                r2 = encryptor.encrypt(block)
                mac_str = mac_encryptor.encrypt(r2)

                # encrypt file and upload
                chunk = aes.encrypt(chunk)
                def job(index, chunk_start, chunk, j):
                    nonlocal exploded
                    if exploded:
                        return
                    class _r:
                        content = b""
                        status_code = 404
                        def close(self):
                            pass
                    try:
                        proxy = {"all": proxies[j]} if proxies[j] else None
                        if proxies[j]:
                            if proxies[j] not in timeout_blacklist:
                                try:
                                    r = requests.post(
                                        ul_url + "/" + str(chunk_start),
                                        data=chunk,
                                        timeout=self.timeout,
                                        proxies=proxy
                                    )
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
                                r = requests.post(ul_url+"/"+str(chunk_start), data=chunk, timeout=self.timeout, proxies=proxy)
                            except:
                                traceback.print_exc()
                                r = _r()
                                r.status_code = 500
                        if r.status_code != 200:
                            if proxies[j]:
                                if proxies[j] not in timeout_blacklist:
                                    timeout_blacklist.append(proxies[j])
                            if (j+1)%len(proxies) != retry_j[index]:
                                # if verbose:
                                #     print("\r", "failed to get chunk", i+1, "out of", l, a, b, ", trying proxy", j+1, "out of", len(proxies))
                                #     print("\r", proxies[j], r.status_code)
                                r.close()
                                job(index, chunk_start, chunk, (j+1)%len(proxies))
                                return
                            else:
                                print("ran out of proxies")
                                r.close()
                                exploded = True
                                return
                        else:
                            completion_file_handle.append(r.text)
                            print("\r", index+1, len(chunks), r.status_code, r.content.decode(), end="")
                            r.close()
                    except:
                        traceback.print_exc()
                        exploded = True
                while not exploded:
                    _ = [int(tw.get_key_by_thread(_)) for tw in tws for _ in tw.threads if _.is_alive()]
                    if not _:
                        break
                    if index-min(_)<min(2**4, parallel_threads):
                        break
                    time.sleep(1)
                while not exploded:
                    j = random.SystemRandom().choice(list(range(0, len(proxies))))
                    # if proxies[j] in timeout_blacklist:
                    #     j = -1
                    if j == -1:
                        time.sleep(1/10)
                    else:
                        break
                retry_j[index] = j
                tws[index%parallel_threads].add(job=def_template(job, index, chunk_start, chunk, j), key=index)
            [tw.wait() for tw in tws]
        else:
            try:
                output_file = requests.post(
                    ul_url + "/0",
                    data='',
                    timeout=self.timeout,
                )
                completion_file_handle.append(output_file.text)
            except:
                exploded = True
                traceback.print_exc()
        input_file.close()
        if exploded:
            raise Exception("upload failed, see trace log above")
        completion_file_handle = [_ for _ in completion_file_handle if _]
        if len(completion_file_handle) != 1:
            raise Exception("unexpected response", completion_file_handle)
        completion_file_handle = completion_file_handle[0]

        logger.info('Chunks uploaded')
        logger.info('Setting attributes to complete upload')
        logger.info('Computing attributes')
        file_mac = str_to_a32(mac_str)

        # determine meta mac
        meta_mac = (file_mac[0] ^ file_mac[1], file_mac[2] ^ file_mac[3])

        dest_filename = dest_filename or os.path.basename(filename)
        attribs = {'n': dest_filename}

        encrypt_attribs = base64_url_encode(
            encrypt_attr(attribs, ul_key[:4]))
        key = [
            ul_key[0] ^ ul_key[4], ul_key[1] ^ ul_key[5],
            ul_key[2] ^ meta_mac[0], ul_key[3] ^ meta_mac[1], ul_key[4],
            ul_key[5], meta_mac[0], meta_mac[1]
        ]
        encrypted_key = a32_to_base64(encrypt_key(key, self.master_key))
        logger.info('Sending request to update attributes')
        # update attributes
        data = self._api_request({
            'a':
                'p',
            't':
                dest,
            'i':
                self.request_id,
            'n': [{
                'h': completion_file_handle,
                't': 0,
                'a': encrypt_attribs,
                'k': encrypted_key
            }]
        })
        logger.info('Upload complete')
        return data

    def sync_files_cache_add(self, file: dict):
        processed_file = self._process_file(file, self.shared_keys)
        parent = processed_file["p"]
        processed_file["path"] = self._local_folders[parent]
        self._files_cache[processed_file["h"]] = processed_file
        self._storage_space_cache["used"] += processed_file["s"]
        # try:
        #     self.export_file(node_id=processed_file["h"])
        # except:
        #     pass

    def sync_files_cache_remove(self, file_id: str):
        self._storage_space_cache["used"] -= self._files_cache[file_id]["s"]
        self._files_cache.pop(file_id)
        
    def upload(self, filename, dest=None, dest_filename=None, auto_split=None, serial_upload=True, parallel_upload=False, parallel_threads=2**3, verbose: bool = True, proxies=None):
        dest = dest or None
        if serial_upload or parallel_upload:
            if verbose:
                print(filename, dest, dest_filename)
        s = os.path.getsize(filename)
        if not self._storage_space_cache:
            self.get_storage_space()
        if parallel_upload:
            r = self.parallel_upload(filename, dest, dest_filename, auto_split, parallel_threads, verbose, proxies)
            self._storage_space_cache["used"] += s
            # self._files_cache = None
            for f in r["f"]:
                self.sync_files_cache_add(f)
            return r
        elif serial_upload:
            r = self.serial_upload(filename, dest, dest_filename)
            self._storage_space_cache["used"] += s
            # self._files_cache = None
            for f in r["f"]:
                self.sync_files_cache_add(f)
            return r
        raise Exception("please specify a upload method: serial_upload or parallel_upload")

    def delete(self, public_handle):
        r = super().delete(public_handle)
        self._files_cache[public_handle]["p"] = self.trashbin_id
        # self._files_cache = None
        return r

    def destroy(self, file_id):
        r = super().destroy(file_id)
        self.sync_files_cache_remove(file_id)
        # self._files_cache = None
        return r

    def empty_trash(self):
        r = super().empty_trash()
        m = [k for k, v in self._files_cache.items() if v["p"] == self.trashbin_id]
        for _ in m:
            self._files_cache.pop(_)
        # self._files_cache = None
        return r

    def rename(self, *args, **kwargs):
        r = super().rename(*args, **kwargs)
        self._files_cache = None
        self._local_folders = None
        return r

    def get_storage_space(self, tera=False, giga=False, mega=False, kilo=False):
        s = 1
        if tera:
            s = 1024*1024*1024*1024
        elif giga:
            s = 1024*1024*1024
        elif mega:
            s = 1024*1024
        elif kilo:
            s = 1024
        if self._storage_space_cache:
            r = self._storage_space_cache
        else:
            r = super().get_storage_space()
            self._storage_space_cache = r
        return {k: v/s for k, v in r.items()}


def batch_wrapper(
        name=None, # type: str
        parallel_threads=2**2, # type: int
        enum=None, # type: list
        job=None, # type: Callable
        validator=lambda v: v, # type: Callable,
        result=None, # type: dict
        verbose=False # type: bool
):
    tw = threadwrapper.ThreadWrapper(threading.Semaphore(parallel_threads))
    if result is None:
        result = {}
    max_retry = max(5, len(enum)//10)
    stop = False
    async_stop = False
    def async_validate():
        nonlocal stop
        while not async_stop:
            if result:
                for _ in result.values():
                    if not validator(_):
                        stop = True
                        return
            time.sleep(1/2)
    p = threading.Thread(target=async_validate)
    p.daemon = True
    p.start()
    class AsyncStopIteration(StopIteration):
        pass
    for i, what in enumerate(list(enum)):
        def t(i, what):
            for j in range(0, max_retry):
                try:
                    if stop:
                        return AsyncStopIteration
                    if verbose:
                        print("\rrunning {}() {}/{} [{}/{}]".format(name, i+1, len(enum), j+1, max_retry), end="")
                    return job(what)
                except:
                    time.sleep(10)
                    if verbose:
                        print("\rretrying {}() {}/{} [{}/{}]".format(name, i+1, len(enum), j+1, max_retry), end="")
                finally:
                    if verbose:
                        print("\rexiting {}() {}/{} [{}/{}]".format(name, i+1, len(enum), j+1, max_retry), end="")
            raise
        if verbose:
            print("\rqueued {}() {}/{}".format(name, i+1, len(enum)), end="")
        tw.add(job=def_template(t, i, what), key=i, result=result)
    tw.wait()
    async_stop = True
    if verbose:
        print("\rvalidating {}()".format(name), end="")
    if not all(validator(_) for _ in result.values() if _ is not AsyncStopIteration):
        raise Exception("some accounts failed to {}, here is list of n-th accounts that failed".format(
            name
        ), [k for k, v in result.items() if not validator(v)])
    if verbose:
        print("\rsorting {}()".format(name), end="")
    keys = sorted(list(result.keys()))
    r = []
    for key in keys:
        r.append(result[key])
    if verbose:
        print("\r", end="")
    return r


class MegaUploaderBase:
    def __init__(
            self,
            accounts = None, # type: list
            verbose = False, # type: bool
            write_cache = False # type: bool
    ):
        self.clients = [] # type: List[Mega]
        self.verbose = verbose
        self.do_write_cache = write_cache
        if accounts:
            self.login(accounts)

    def batch_wrapper(self, **kwargs):
        if "enum" not in kwargs:
            kwargs["enum"] = list(range(len(self.clients)))
        return batch_wrapper(verbose=self.verbose, **kwargs)

    def login(self, accounts):
        def job(account):
            try:
                client = Mega()
                if isinstance(account, list):
                    client.login(*account)
                else:
                    _ = json.loads(account)
                    sid, master_key = _[:2]
                    client.sid = sid
                    client.master_key = master_key
                    if len(_) == 9:
                        client.shared_keys = _[2]
                        client.root_id = _[3]
                        client.inbox_id = _[4]
                        client.trashbin_id = _[5]
                        client._files_cache = _[6]
                        client._local_folders = _[7]
                        client._storage_space_cache = _[8]
                return client
            except:
                # import traceback
                # traceback.print_exc()
                return None
        result = {}
        try:
            self.clients = self.batch_wrapper(name="login", enum=accounts, job=job, result=result)
        except Exception as e:
            clients = [None]*len(accounts)
            keys = sorted(list(result.keys()))
            for key in keys:
                clients[key] = result[key]
            open("sessions.cache", "wb").write(b64e(pickle.dumps([json.dumps([
                cl.sid,
                cl.master_key,
                cl.shared_keys,
                cl.root_id,
                cl.inbox_id,
                cl.trashbin_id,
                cl._files_cache,
                cl._local_folders,
                cl._storage_space_cache
            ]) if isinstance(cl, Mega) else ac for ac, cl in zip(accounts, clients)])).encode())
            raise e
        if self.do_write_cache:
            self.write_cache()
        return True

    def write_cache(self, parent: str = None):
        fp = "sessions.cache"
        if parent:
            fp = os.path.join(parent, fp)
        open(fp, "wb").write(
            b64e(pickle.dumps([json.dumps([
                _.sid,
                _.master_key,
                _.shared_keys,
                _.root_id,
                _.inbox_id,
                _.trashbin_id,
                _._files_cache,
                _._local_folders,
                _._storage_space_cache
            ]) for _ in self.clients])).encode()
        )

    def clear_cache(self):
        for _ in self.clients:
            _._files_cache = None
            _._local_folders = None
            _._storage_space_cache = None

    def logout(self):
        self.clients.clear()
        return True

    def _get_quota(self, clients_i: int):
        return self.clients[clients_i].get_quota()

    def _get_storage_space(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].get_storage_space(*args, **kwargs)

    def _get_balance(self, clients_i: int):
        return self.clients[clients_i].get_balance()

    def _get_files(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].get_files(*args, **kwargs)

    def _get_user(self, clients_i: int):
        return self.clients[clients_i].get_user()

    def _filter(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].filter(*args, **kwargs)

    def _find(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].find(*args, **kwargs)

    def _findall(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].findall(*args, **kwargs)

    def _destroy(self, clients_i: int, file_id: str):
        self.clients[clients_i].destroy(file_id)

    def _delete(self, clients_i: int, file_id: str):
        self.clients[clients_i].delete(file_id)

    def _create_folder(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].create_folder(*args, **kwargs)

    def _upload(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].upload(*args, **kwargs)

    def _get_items_in_folder(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].get_items_in_folder(*args, **kwargs)

    def _export(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].export(*args, **kwargs)

    def _export_file(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].export_file(*args, **kwargs)

    def _export_folder(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].export_folder(*args, **kwargs)

    def _revoke(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].revoke(*args, **kwargs)

    def _revoke_file(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].revoke_file(*args, **kwargs)

    def _revoke_folder(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].revoke_folder(*args, **kwargs)

    def _move(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].move(*args, **kwargs)

    def _import_url(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].import_url(*args, **kwargs)

    def _download(self, clients_i: int, *args, **kwargs):
        return self.clients[clients_i].download(*args, **kwargs)





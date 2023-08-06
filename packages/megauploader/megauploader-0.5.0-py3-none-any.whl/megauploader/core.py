from omnitools import create_cascade, format_cascade, b64e, b64d
from .utils import MegaUploaderBase, FindResult
from datetime import datetime
from typing import overload
import traceback
import random
import math
import json
import os
import re
from typing import List


class MegaUploader(MegaUploaderBase):
    def get_quota(self):
        def job(clients_i):
            try:
                return self._get_quota(clients_i)
            except:
                return -1
        def validator(v):
            return v != -1
        return self.batch_wrapper(name="get_quota", job=job, validator=validator)

    def get_storage_space(self, *args, **kwargs):
        def job(clients_i):
            try:
                return self._get_storage_space(clients_i, *args, **kwargs) or {}
            except:
                return None
        def validator(v):
            return v is not None
        try:
            return self.batch_wrapper(name="get_storage_space", job=job, validator=validator)
        except Exception as e:
            raise e
        finally:
            self.write_cache()

    def get_balance(self):
        def job(clients_i):
            try:
                return self._get_balance(clients_i)
            except:
                return -1
        def validator(v):
            return v != -1
        return self.batch_wrapper(name="get_balance", job=job, validator=validator)

    def get_files(self, *args, **kwargs):
        def job(clients_i):
            try:
                return self._get_files(clients_i, *args, **kwargs) or {}
            except:
                return None
        def validator(v):
            return v is not None
        try:
            r = self.batch_wrapper(name="get_files", job=job, validator=validator)
        except Exception as e:
            raise e
        finally:
            self.write_cache()
        return [[FindResult(_) for _ in rr.items()] for rr in r]

    def get_user(self):
        def job(clients_i):
            try:
                return self._get_user(clients_i) or {}
            except:
                return None
        def validator(v):
            return v is not None
        return self.batch_wrapper(name="get_user", job=job, validator=validator)

    def filter(self, *args, **kwargs) -> List[List[FindResult]]:
        self.get_files()
        def job(clients_i):
            try:
                return self._filter(clients_i, *args, **kwargs) or []
            except:
                return None
        def validator(v):
            return v is not None
        r = self.batch_wrapper(name="find", job=job, validator=validator)
        return [[FindResult(_) for _ in rr] for rr in r]

    def find(self, *args, **kwargs) -> List[List[FindResult]]:
        self.get_files()
        def job(clients_i):
            try:
                return self._find(clients_i, *args, **kwargs) or []
            except:
                return None
        def validator(v):
            return v is not None
        r = self.batch_wrapper(name="find", job=job, validator=validator)
        return [[FindResult(_)] if _ else [] for _ in r]

    def findall(self, *args, **kwargs) -> List[List[FindResult]]:
        self.get_files()
        def job(clients_i):
            try:
                return self._findall(clients_i, *args, **kwargs) or []
            except:
                return None
        def validator(v):
            return v is not None
        r = self.batch_wrapper(name="findall", job=job, validator=validator)
        return [[FindResult(_) for _ in rr] for rr in r]

    def destroy(self, find_result: List[List[FindResult]]):
        def job(find_result):
            try:
                clients_i, find_result = find_result
                for _ in find_result:
                    self._destroy(clients_i, _.file_id)
                return True
            except:
                return None
        return self.batch_wrapper(name="destroy", enum=list(enumerate(find_result)), job=job)

    def delete(self, find_result: List[List[FindResult]]):
        def job(find_result):
            try:
                clients_i, find_result = find_result
                for _ in find_result:
                    self._delete(clients_i, _.file_id)
                return True
            except:
                return None
        return self.batch_wrapper(name="delete", enum=list(enumerate(find_result)), job=job)

    def create_folder(self, *args, **kwargs):
        def job(clients_i):
            try:
                return self._create_folder(clients_i, *args, **kwargs)
            except:
                # print(clients_i, traceback.format_exc(), "\n\n", flush=True)
                return None
        return self.batch_wrapper(name="create_folder", job=job)

    def upload(self, filename: str, dest=None, dest_filename=None, overwrite: bool = False, skip_nospace: bool = False, auto_split: list = None, auto_split_step: int = 1000*1000*1000*2, **kwargs):
        dest = dest or None
        remote_fp = dest_filename or os.path.basename(filename)
        if dest:
            remote_fp = "/".join([dest, remote_fp])
        file_size = os.path.getsize(filename)
        r0 = self.find(remote_fp)
        if not file_size and not any(r0):
            r0 = [[__ for __ in _ if __.file_data["t"] == 0 and "s" in __.file_data and (__.file_data["path"]+__.file_data["a"]["n"]).startswith("/"+remote_fp+".megapy_part")] for _ in self.get_files(exclude_deleted=True)]
        rs = []
        # print("uploader upload", remote_fp, r0)
        if any(r0):
            if overwrite:
                self.destroy(r0)
            else:
                if self.verbose:
                    print("uploader upload", "exists")
                return r0
        if isinstance(auto_split, list):
            file_size = auto_split[1]-auto_split[0]
        storage_space = self.get_storage_space()
        clients_i = []
        for i, _ in enumerate(storage_space):
            if _["total"]-_["used"]>=file_size:
                clients_i.append(i)
        if not clients_i:
            if auto_split is True:
                splits = [[i, min(i+auto_split_step, file_size)] for i in range(0, math.ceil(file_size/auto_split_step)*auto_split_step, auto_split_step)]
                for i, split in enumerate(splits):
                    rs.extend(self.upload(filename, dest, (dest_filename or os.path.basename(filename))+".megapy_part{}".format(str(i).zfill(5)), overwrite, skip_nospace, split, **kwargs))
                return rs
            elif skip_nospace:
                if self.verbose:
                    print("skipped", filename, file_size)
                return
            else:
                raise Exception("failed to upload {}, no available account with remaining space of {} KB".format(
                    filename,
                    file_size
                ))
        random.SystemRandom().choice(clients_i)
        clients_i = random.SystemRandom().choice(clients_i)
        if dest:
            # print("cache", [not not _._files_cache for _ in self.clients])
            # folders = self.create_folder(dest)
            dest = self._create_folder(clients_i, dest)[-1][1]
            # print("cache", [not not _._files_cache for _ in self.clients])
            # dest = [_[-1][1] for _ in folders][clients_i]
        r = [None]*len(storage_space)
        # print("uploader upload", clients_i, dest, file_size)
        if not isinstance(auto_split, list):
            auto_split = None
        # print("cache", [not not _._files_cache for _ in self.clients])
        r[clients_i] = self._upload(clients_i, filename, dest, dest_filename, auto_split, verbose=self.verbose, **kwargs)
        # print("cache", [not not _._files_cache for _ in self.clients])
        # print("uploader uploaded", filename)
        rs.append(r)
        return rs

    def get_items_in_folder(self, *args, **kwargs) -> List[List[FindResult]]:
        def job(clients_i):
            try:
                return self._get_items_in_folder(clients_i, *args, **kwargs) or {}
            except:
                return None
        def validator(v):
            return v is not None
        r = self.batch_wrapper(name="get_items_in_folder", job=job, validator=validator)
        return [[FindResult(_) for _ in rr.items()] for rr in r]

    def export(self, *args, **kwargs):
        def job(clients_i):
            try:
                try:
                    r = self._export(clients_i, *args, **kwargs)
                    # print(r)
                    return r
                except Exception as e:
                    if "cannot find" in str(e):
                        return ""
                    else:
                        # import traceback
                        # traceback.print_exc()
                        raise
            except:
                return None
        def validator(v):
            return v is not None
        return self.batch_wrapper(name="export", job=job, validator=validator)

    def export_file(self, *args, **kwargs):
        def job(clients_i):
            try:
                try:
                    return self._export_file(clients_i, *args, **kwargs)
                except Exception as e:
                    if "cannot find" in str(e):
                        return ""
                    else:
                        raise
            except:
                return None
        def validator(v):
            return v is not None
        return self.batch_wrapper(name="export_file", job=job, validator=validator)

    def export_folder(self, *args, **kwargs):
        def job(clients_i):
            try:
                try:
                    return self._export_folder(clients_i, *args, **kwargs)
                except Exception as e:
                    if "cannot find" in str(e):
                        return ""
                    else:
                        raise
            except:
                return None
        def validator(v):
            return v is not None
        return self.batch_wrapper(name="export_folder", job=job, validator=validator)

    def revoke(self, *args, **kwargs):
        self.get_files()
        def job(clients_i):
            try:
                try:
                    return self._revoke(clients_i, *args, **kwargs)
                except Exception as e:
                    if "cannot find" in str(e):
                        return True
                    else:
                        raise
            except:
                return None
        return self.batch_wrapper(name="revoke", job=job)

    def revoke_file(self, *args, **kwargs):
        self.get_files()
        def job(clients_i):
            try:
                try:
                    return self._revoke_file(clients_i, *args, **kwargs)
                except Exception as e:
                    if "cannot find" in str(e):
                        return True
                    else:
                        raise
            except:
                return None
        return self.batch_wrapper(name="revoke_file", job=job)

    def revoke_folder(self, *args, **kwargs):
        self.get_files()
        def job(clients_i):
            try:
                try:
                    return self._revoke_folder(clients_i, *args, **kwargs)
                except Exception as e:
                    if "cannot find" in str(e):
                        return True
                    else:
                        raise
            except:
                return None
        return self.batch_wrapper(name="revoke_folder", job=job)

    def move(self, *args, **kwargs):
        def job(clients_i):
            try:
                return self._move(clients_i, *args, **kwargs)
            except:
                import traceback
                traceback.print_exc()
                return None
        return self.batch_wrapper(name="move", job=job)

    def import_url(self, url: str, dest_path: str = None, dest_name: str = None):
        self.get_files()
        tmp_client = self.clients[0]
        total_size = None
        try:
            tmp_client.parse_folder_url(url)
        except:
            pass
        else:
            files = tmp_client.get_files_in_folder(url, include_folders=True)
            total_size = sum([_["s"] for _ in files if _["t"] == 0])
        try:
            file_handle, file_key = tmp_client._parse_url(url).split('!')
        except:
            pass
        else:
            pl_info = tmp_client.get_public_file_info(file_handle, file_key)
            total_size = pl_info['size']
        if total_size is None:
            raise Exception("cannot import url ({}) due to cannot get total size".format(url))
        r = [None]*len(self.clients)
        if total_size:
            storage_space = self.get_storage_space()
            clients_i = []
            for i, _ in enumerate(storage_space):
                if _["total"]-_["used"]>=total_size:
                    clients_i.append(i)
            if not clients_i:
                raise Exception("cannot import url ({}) due to no remaining space in cluster".find(url))
            random.SystemRandom().choice(clients_i)
            clients_i = random.SystemRandom().choice(clients_i)
            r[clients_i] = self._import_url(clients_i, url, dest_path, dest_name)
        return r

    def download(self, files: List[List[FindResult]], *args, **kwargs):
        for clients_i, find_results in enumerate(files):
            for find_result in find_results:
                self._download(clients_i, find_result, *args, **kwargs)


class MegaManager:
    def __init__(
            self,
            accounts = None, # type: list
            verbose = False, # type: bool
            write_cache = False # type: bool
    ):
        self.mu = MegaUploader(accounts, verbose, write_cache)

    def print_FindResult(self, r: List[List[FindResult]]):
        global_files = []
        for i, _ in enumerate(r):
            for find_result in _:
                if find_result.file_data["t"] == 0:
                    find_result.file_data["pi"] = i
                    global_files.append([find_result.file_data["path"]+find_result.file_data["a"]["n"], find_result])
        # print(r[0][1].file_data)
        r0 = [math.floor(math.log(b.file_data["s"] or 1)/math.log(1024)) for a, b in global_files]
        r1 = [[a, b.file_data["s"]] for a, b in global_files]
        r = [[
            a,
            b.file_id,
            str(b.file_data["pi"]),
            "{:.2f} {}B".format(b.file_data["s"]/(1024**exp), ["", "Ki", "Mi", "Gi", "Ti"][exp]),
            str(datetime.fromtimestamp(b.file_data["ts"]).strftime("%Y-%m-%d %H:%M:%S")),
        ] for (a,b), exp in zip(global_files, r0)]
        r_max = ["{{:{}{}}}".format(
            "^" if i in [0,1,3] else ">",
            12 if i in [0,1,2] else len(max(_, key=len))
        ) for i, _ in enumerate(list(zip(*r))[1:])]
        r = [[
            a,
            r_max[0].format(b),
            r_max[1].format(c),
            r_max[2].format(d),
            r_max[3].format(e),
        ] for a,b,c,d,e in r]
        cascade = create_cascade(r, key=0, sep="/")
        formatted = format_cascade(cascade, key=0, sep="/", f_sep=" | ")
        formatted = "\n".join(" | " + _ for _ in formatted.splitlines())
        t = [[__ for __ in _.split(" | ", 5)] for _ in formatted.splitlines()]
        # [print(_) for _ in t]
        paths = []
        pp = None
        for i in range(0, len(t)):
            if not t[i][3].strip(" ") and t[i][5]:
                size = 0
                p = re.search(r"^([\|\'\- ]+) (.*?)$", t[i][5])
                ps = p[1]
                p = p[2]
                if not paths:
                    paths.append(p)
                else:
                    if len(ps) < len(pp):
                        for o in range(0, (len(pp)-len(ps))//4+1):
                            paths.pop(-1)
                    elif len(ps) == len(pp):
                        paths.pop(-1)
                    paths.append(p)
                for a, b in r1:
                    if a.startswith("/".join([""]+paths+[""])):
                        size += b
                if size:
                    exp = math.floor(math.log(size)/math.log(1024))
                    fs = "{:.2f} {}B".format(size/(1024**exp), ["", "Ki", "Mi", "Gi", "Ti"][exp])
                else:
                    fs = ""
                t[i][3] = r_max[2].format(fs)
                pp = ps
            t[i] = " | ".join(t[i])
        formatted = "\n".join(t)
        heading = " | ".join([
            "",
            r_max[0].replace(":>", ":^").format("file id"),
            r_max[1].replace(":>", ":^").format("cluster"),
            r_max[2].replace(":>", ":^").format("size"),
            r_max[3].replace(":>", ":^").format("timestamp"),
            "file name"+" "*18
        ])
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(heading)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(formatted)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))

    def quit(self):
        return self.mu.logout()

    def get_quota(self):
        return self.mu.get_quota()

    def print_quota(self):
        quota = list(enumerate(self.get_quota()))
        summary = [
            "summary",
            sum(_ for __, _ in quota)
        ]
        max_cols = [12 if i in [0,1] else len(str(max(_, key=lambda x: len(str(x))))) for i, _ in enumerate(zip(*quota))]
        max_cols = ["{{:{}{}}}".format(
            "^" if i in [0] else ">",
            _
        ) for i, _ in enumerate(max_cols)]
        # print(quota, max_cols)
        heading = " | ".join([
            "",
            max_cols[0].replace(":>", ":^").format("cluster"),
            max_cols[1].replace(":>", ":^").format("quota"),
            ""
        ])
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(heading)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        for _ in quota:
            line = " | ".join([
                "",
                max_cols[0].format(_[0]),
                max_cols[1].format("{} MB".format(_[1])),
                ""
            ])
            print(line)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(" | ".join([
            "",
            max_cols[0].format(summary[0]),
            max_cols[1].format("{} MB".format(summary[1])),
            ""
        ]))
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))

    def get_storage_space(self, *args, **kwargs):
        return self.mu.get_storage_space(*args, **kwargs)

    def print_storage_space(self, *args, **kwargs):
        storage_space = self.get_storage_space(*args, **kwargs)
        summary = [
            "summary",
            "{:.2f}".format(sum(_["used"] for _ in storage_space)),
            "{:.2f}".format(sum(_["total"]-_["used"] for _ in storage_space)),
            "{:.2f}".format(sum(_["total"] for _ in storage_space))
        ]
        storage_space = [[
            i,
            "{:.2f}".format(_["used"]),
            "{:.2f}".format(_["total"]-_["used"]),
            "{:.2f}".format(_["total"])
        ] for i, _ in enumerate(storage_space)]
        max_cols = [12 if i in [0] else len(str(max(_, key=lambda x: len(str(x)))))+3 for i, _ in enumerate(zip(*storage_space))]
        max_cols = ["{{:{}{}}}".format(
            "^" if i in [0] else ">",
            _,
        ) for i, _ in enumerate(max_cols)]
        # print(storage_space, max_cols)
        heading = " | ".join([
            "",
            max_cols[0].replace(":>", ":^").format("cluster"),
            max_cols[1].replace(":>", ":^").format("used"),
            max_cols[2].replace(":>", ":^").format("free"),
            max_cols[3].replace(":>", ":^").format("total"),
            ""
        ])
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(heading)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        for _ in storage_space:
            line = " | ".join([
                "",
                max_cols[0].format(_[0]),
                max_cols[1].format(_[1]),
                max_cols[2].format(_[2]),
                max_cols[3].format(_[3]),
                ""
            ])
            print(line)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(" | ".join([
            "",
            max_cols[0].format(summary[0]),
            max_cols[1].format(summary[1]),
            max_cols[2].format(summary[2]),
            max_cols[3].format(summary[3]),
            ""
        ]))
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))

    def get_balance(self):
        return self.mu.get_balance()

    def print_balance(self):
        balance = list(enumerate(self.get_balance()))
        max_cols = [12 if i in [0,1] else len(str(max(_, key=lambda x: len(str(x))))) for i, _ in enumerate(zip(*balance))]
        max_cols = ["{{:{}{}}}".format(
            "^" if i in [0] else ">",
            _
        ) for i, _ in enumerate(max_cols)]
        # print(balance, max_cols)
        heading = " | ".join([
            "",
            max_cols[0].replace(":>", ":^").format("cluster"),
            max_cols[1].replace(":>", ":^").format("balance"),
            ""
        ])
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        print(heading)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))
        for _ in balance:
            line = " | ".join([
                "",
                max_cols[0].format(_[0]),
                max_cols[1].format("{} MB".format(_[1])),
                ""
            ])
            print(line)
        print(re.sub(r"[^\-\+]", "-", heading.replace(" | ", " + ")))

    def get_user(self):
        return self.mu.get_user()

    def get_files(self, *args, **kwargs):
        return self.mu.get_files(*args, **kwargs)

    def print_files(self, *args, **kwargs):
        if "r" not in kwargs:
            r = self.get_files(*args, **kwargs)
        else:
            r = kwargs["r"]
        self.print_FindResult(r)

    def filter(self, *args, **kwargs):
        return self.mu.filter(*args, **kwargs)

    def print_filter(self, *args, **kwargs):
        if "r" not in kwargs:
            r = self.filter(*args, **kwargs)
        else:
            r = kwargs["r"]
        self.print_FindResult(r)

    def find(self, *args, **kwargs):
        return self.mu.find(*args, **kwargs)

    def print_find(self, *args, **kwargs):
        if "r" not in kwargs:
            r = self.find(*args, **kwargs)
        else:
            r = kwargs["r"]
        self.print_FindResult(r)

    def findall(self, *args, **kwargs):
        return self.mu.findall(*args, **kwargs)

    def print_findall(self, *args, **kwargs):
        if "r" not in kwargs:
            r = self.findall(*args, **kwargs)
        else:
            r = kwargs["r"]
        self.print_FindResult(r)

    def destroy(self, *args, **kwargs):
        return self.mu.destroy(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.mu.delete(*args, **kwargs)

    def upload(self, root: str, path: str, dest_filename: str=None, **kwargs):
        fp = os.path.join(root, path)
        results = []
        if os.path.isfile(fp):
            path = "/"+path.replace("\\", "/").strip("/")
            print("manager upload", fp)
            dest = os.path.dirname(path)
            results.extend(self.mu.upload(fp, dest=None if dest == "/" else dest, dest_filename=dest_filename, **kwargs))
            print("manager uploaded", fp)
        elif os.path.isdir(fp):
            for a, b, c in os.walk(fp):
                for d in c:
                    e = os.path.join(a, d)
                    _path = e.replace(root, "")
                    if _path[0] in ["/", "\\"]:
                        _path = _path[1:]
                    # print(root, _path)
                    results.extend(self.upload(root, _path, None, **kwargs))
        else:
            raise ValueError("unknown path for", root, path)
        return results

    def get_items_in_folder(self, *args, **kwargs):
        return self.mu.get_items_in_folder(*args, **kwargs)

    def print_items_in_folder(self, *args, **kwargs):
        if "r" not in kwargs:
            r = self.get_items_in_folder(*args, **kwargs)
        else:
            r = kwargs["r"]
        self.print_FindResult(r)

    def export_to_universal(self, urls):
        urls = [_.replace("https://mega.co.nz/", "") for _ in urls if _]
        return b64e(json.dumps(urls))

    def export_universal(self, *args, **kwargs):
        return self.export_to_universal(self.export(*args, **kwargs))

    def import_universal(self, base64_string: str, dest_path: str = None):
        w = json.loads(b64d(base64_string).decode())
        w = ["https://mega.co.nz/"+_ for _ in w if _]
        return self.import_urls(w, dest_path)

    def export(self, *args, **kwargs):
        return self.mu.export(*args, **kwargs)

    def revoke(self, *args, **kwargs):
        return self.mu.revoke(*args, **kwargs)

    def move(self, *args, **kwargs):
        return self.mu.move(*args, **kwargs)

    def import_url(self, *args, **kwargs):
        return self.mu.import_url(*args, **kwargs)

    def import_urls(self, urls: list, dest_path):
        r = [[] for i in range(0, len(self.mu.clients))]
        for url in urls:
            if not url:
                continue
            print("\rimporting url ({}) out of {} urls".format(url, len(urls)), end="")
            _r = self.import_url(url, dest_path)
            for a, b in zip(r, _r):
                if b is not None:
                    a.append(b)
        print("\r", end="")
        return r

    def download(self, *args, **kwargs):
        return self.mu.download(*args, **kwargs)

    def write_cache(self, *args, **kwargs):
        return self.mu.write_cache(*args, **kwargs)

    def clear_cache(self):
        return self.mu.clear_cache()




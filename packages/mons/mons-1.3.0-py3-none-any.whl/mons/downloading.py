import os
import shutil
import typing as t
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
from contextlib import nullcontext
from io import BytesIO
from tempfile import TemporaryDirectory

import urllib3
from click import Abort
from tqdm import tqdm
from urllib3.exceptions import HTTPError

from mons import baseUtils
from mons import fs
from mons.baseUtils import read_with_progress
from mons.modmeta import ModDownload
from mons.modmeta import UpdateInfo


def get_download_size(url: str, initial_size: int = 0, http_pool=None):
    http = http_pool or urllib3.PoolManager()
    return int(http.request("HEAD", url).headers["Content-Length"]) - initial_size


def download_with_progress(
    src: t.Union[str, urllib.request.Request, urllib3.HTTPResponse],
    dest: t.Optional[str],
    label: t.Optional[str] = None,
    atomic: t.Optional[bool] = False,
    clear: t.Optional[bool] = False,
    *,
    response_handler=None,
    pool_manager=None,
):
    if not dest and atomic:
        raise ValueError("atomic download cannot be used without destination file")

    http = pool_manager or urllib3.PoolManager()

    response = (
        http.request(
            "GET",
            src,
            preload_content=False,
            timeout=urllib3.Timeout(connect=3, read=10),
        )
        if isinstance(src, (str, urllib.request.Request))
        else src
    )

    content = response_handler(response) if response_handler else response
    size = int(response.headers.get("Content-Length", None) or 100)
    blocksize = 8192

    with fs.temporary_file(persist=False) if atomic else nullcontext(dest) as file:
        with open(file, "wb") if file else nullcontext(BytesIO()) as io:
            read_with_progress(content, io, size, blocksize, label, clear)

            if dest is None and isinstance(io, BytesIO):
                # io will not be closed by contextmanager because it used nullcontext
                io.seek(0)
                return io

        if atomic:
            dest = t.cast(str, dest)
            if os.path.isfile(dest):
                os.remove(dest)
            shutil.move(t.cast(str, file), dest)

    return BytesIO()


def downloader(src, dest, name, mirror=None, http_pool=None):
    mirror = mirror or src

    if os.path.isdir(dest):
        tqdm.write(f"\nCould not overwrite unzipped mod: {os.path.basename(dest)}")
    try:
        download_with_progress(
            src, dest, f"{name} {src}", atomic=True, clear=True, pool_manager=http_pool
        )
    except Abort:
        return
    except Exception as e:
        tqdm.write(f"\nError downloading file {os.path.basename(dest)} {src}: {e}")
        if isinstance(e, (HTTPError)) and src != mirror:
            downloader(mirror, dest, name)


def mod_downloader(mod_folder, download: t.Union[ModDownload, UpdateInfo], http_pool):
    if isinstance(download, ModDownload):
        src, mirror, dest, name = (
            download.Url,
            download.Mirror,
            os.path.join(mod_folder, download.Meta.Name + ".zip"),
            str(download.Meta),
        )
    else:
        src, mirror, dest, name = (
            download.Url,
            download.Mirror,
            download.Old.Path,
            str(download.Old),
        )

    downloader(src, dest, name, mirror, http_pool)


def download_threaded(
    mod_folder,
    downloads: t.Sequence[t.Union[ModDownload, UpdateInfo]],
    late_downloads=None,
    thread_count=8,
):
    http_pool = urllib3.PoolManager(maxsize=thread_count)
    with ThreadPoolExecutor(
        max_workers=thread_count, thread_name_prefix="download_"
    ) as pool:
        futures = [
            pool.submit(mod_downloader, mod_folder, download, http_pool)
            for download in downloads
        ]
        with TemporaryDirectory("_mons") if late_downloads else nullcontext(
            ""
        ) as temp_dir:
            if late_downloads:
                futures += [
                    pool.submit(mod_downloader, temp_dir, download, http_pool)
                    for download in late_downloads
                ]
            try:
                while True:
                    _, not_done = wait(futures, timeout=0.1)
                    if len(not_done) < 1:
                        break
            except (KeyboardInterrupt, SystemExit):
                for future in futures:
                    future.cancel()
                baseUtils._download_interrupt = True
                raise

            if late_downloads:
                for file in os.listdir(temp_dir):
                    shutil.move(os.path.join(temp_dir, file), mod_folder)

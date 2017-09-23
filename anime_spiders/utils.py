# -*- coding: utf-8 -*-
import os

import requests

from .settings import DOWNLOAD_TIMEOUT


def download_file(file_url, file_full_name, spider=None, headers=None):
    tmp_name = file_full_name + '.tmp'
    try:
        with open(tmp_name, 'wb') as f:
            rsp = requests.get(file_url, timeout=DOWNLOAD_TIMEOUT, headers=headers)
            for chunk in rsp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except Exception as e:
        os.remove(tmp_name)
        raise e
    else:
        os.rename(tmp_name, file_full_name)


def prepare_download(file_url, spider=None, file_dir=None):
    if not file_url:
        return
    if not file_url.startswith('http'):
        file_url = spider.get_full_url(file_url)
    url_domain = file_url.lstrip('http://').lstrip('https://')\
                         .lstrip('//').split('/')[0]
    file_name = file_url.rsplit('/', 1)[-1]

    if not file_dir:
        file_dir = os.path.join('.storage', url_domain.replace('.', '_'))
    else:
        file_dir = os.path.join('.storage', file_dir)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    file_full_name = os.path.join(file_dir, file_name)
    return file_full_name

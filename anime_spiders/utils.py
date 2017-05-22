# -*- coding: utf-8 -*-
import os

import requests


def download_file(file_url, file_full_name, spider=None):
    try:
        with open(file_full_name, 'wb') as f:
            for chunk in requests.get(file_url).iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except KeyboardInterrupt:
        os.remove(file_full_name)


def prepare_download(file_url, spider):
    if not file_url:
        return
    file_url = spider.get_full_url(file_url)
    url_domain = file_url.lstrip('http://').lstrip('https://')\
                .lstrip('//').split('/')[0]
    file_name = file_url.rsplit('/', 1)[-1]
    file_dir = os.path.join('.storage', url_domain.replace('.', '_'))

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    file_full_name = os.path.join(file_dir, file_name)
    return file_full_name

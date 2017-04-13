# -*- coding: utf-8 -*-
import os

import requests


class FilesPipeline(object):

    def process_item(self, item, spider):

        file_urls = item.get_file_urls()

        for file_url in file_urls:
            if not file_url:
                continue
            file_name = file_url.rsplit('/', 1)[-1]
            file_dir = os.path.join('.storage', spider.name)

            if not os.path.exists(file_dir):
                os.makedirs(file_dir)

            file_full_name = os.path.join(file_dir, file_name)

            if os.path.exists(file_full_name):
                continue

            with open(file_full_name, 'wb') as f:
                for chunk in requests.get(file_url).iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        return item

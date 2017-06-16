# -*- coding: utf-8 -*-
import os

import django

from .utils import download_file, prepare_download


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exhibition.settings")

django.setup()


class DjangoItemPipeline(object):
    def process_item(self, item, spider):
        item.save()
        return item


class CGTagsPipeline(object):
    def process_item(self, item, spider):
        tags = item['tags_string'].split(' ')
        item.tags.add(*tags)
        return item


class AnimeTagsPipeline(object):
    def process_item(self, item, spider):
        item.instance.assit_companies.add(*item['assit_companies'])
        tag_fields = [
            'assit_companies',
            'directors',
            'scenarists',
            'effect_makers',
            'audio_directors',
            'main_animators',
            'photo_directors',
            'mechanical_designers',
            'anime_directors',
            'charactor_designers',
            'storyboard_directors',
            'acts',
            'musicians',
        ]
        for field in tag_fields:
            tag = getattr(item.instance, field)
            tag.add(*item[field])
        return item


class ShortVideoTagsPipeline(object):
    def process_item(self, item, spider):
        tags = item['tags_string'].split(' ')
        item.instance.tags.add(*tags)
        return item


class BangumiTVCoverPipeline(object):
    def process_item(self, item, spider):
        cover_url = item['cover']
        if not cover_url:
            return item
        cover_url = 'http:' + item['cover']
        file_full_name = prepare_download(cover_url, spider)

        if not os.path.exists(file_full_name):
            download_file(cover_url, file_full_name, spider=spider)
        item['cover_path'] = file_full_name
        return item


class TorrentDownloadPipeline(object):
    def process_item(self, item, spider):
        if not item['torrent']:
            return item

        torrent_url = spider.get_full_url(item['torrent'])
        file_full_name = prepare_download(torrent_url, spider)
        if os.path.exists(file_full_name):
            return item
        download_file(torrent_url, file_full_name, spider=spider)
        item['torrent_path'] = file_full_name
        return item


class ShortVideoDownloadPipeline(object):
    def process_item(self, item, spider):
        if item['file_url']:
            file_full_name = prepare_download(item['file_url'], spider)
            if not os.path.exists(file_full_name):
                download_file(item['file_url'], file_full_name, spider=spider)
            item['file_path'] = file_full_name

        if item['preview_url']:
            file_full_name = prepare_download(item['preview_url'], spider)
            if not os.path.exists(file_full_name):
                download_file(item['preview_url'], file_full_name, spider=spider)
            item['preview_path'] = file_full_name
        return item

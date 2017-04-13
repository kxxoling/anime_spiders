# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exhibition.settings")
import django       # noqa
django.setup()

from scrapy import Field                    # noqa
from scrapy_djangoitem import DjangoItem    # noqa

from exhibition import models               # noqa


class BasicItem(DjangoItem):
    pass


class Torrent(BasicItem):
    django_model = models.Torrent

    crawled_from = Field()
    site = Field()
    site_pk = Field()
    title = Field()
    team_name = Field()
    team_id = Field()
    size = Field()
    torrent = Field()
    magnet = Field()
    link = Field()
    pub_date = Field()
    author = Field()
    category = Field()

    def get_file_urls(self):
        return [self['torrent']]


class Anime(BasicItem):
    django_model = models.Anime

    crawled_from = Field()
    site_pk = Field()
    link = Field()
    cover = Field()
    name = Field()
    orig_name = Field()
    pub_date = Field()

    def get_file_urls(self):
        return [self['cover']]


class CG(BasicItem):
    django_model = models.CG

    crawled_from = Field()
    large_file_url = Field()
    file_url = Field()
    source = Field()
    site_pk = Field()
    tags_string = Field()
    md5 = Field()
    pixiv_id = Field()

    def get_file_urls(self):
        return [self['large_file_url'], self['file_url']]


class ShortVideo(BasicItem):
    django_model = models.ShortVideo

    crawled_from = Field()
    site_pk = Field()
    md5 = Field()
    preview_url = Field()
    file_url = Field()
    file_size = Field()
    tags = Field()
    author = Field()
    source = Field()
    score = Field()
    file_ext = Field()

    def get_file_urls(self):
        return [self['file_url'], self['preview_url']]

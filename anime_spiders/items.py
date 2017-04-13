# -*- coding: utf-8 -*-
from scrapy import Item, Field


class Torrent(Item):
    site = Field()
    id = Field()
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


class Anime(Item):
    id = Field()
    link = Field()
    cover = Field()
    name = Field()
    orig_name = Field()
    pub_date = Field()

    def get_file_urls(self):
        return [self['cover']]


class CG(Item):
    large_file_url = Field()
    file_url = Field()
    source = Field()
    id = Field()
    tags_string = Field()
    md5 = Field()
    pixiv_id = Field()

    def get_file_urls(self):
        return [self['large_file_url'], self['file_url']]


class ShortVideo(Item):
    id = Field()
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

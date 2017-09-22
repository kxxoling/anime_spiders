# -*- coding: utf-8 -*-
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exhibition.settings")
import django       # noqa
django.setup()

from scrapy import Field                    # noqa
from scrapy_djangoitem import DjangoItem    # noqa

from exhibition import models               # noqa


class BasicItem(DjangoItem):
    @property
    def instance(self):
        if self._instance is None:
            self._instance, _ = self.django_model.objects.get_or_create(
                site_pk=self['site_pk'],
                crawled_from=self['crawled_from'])
            modelargs = dict((k, self.get(k)) for k in self._values
                             if k in self._model_fields and not isinstance(self.get(k), list))
            for k, v in modelargs.items():
                setattr(self._instance, k, v)
        return self._instance


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

    torrent_path = Field()


class Anime(BasicItem):
    django_model = models.Anime

    crawled_from = Field()
    site_pk = Field()
    link = Field()
    cover = Field()
    name = Field()
    orig_name = Field()
    pub_date = Field()

    cover_path = Field()

    alter_names = Field()
    episode_length = Field()

    company = Field()
    assit_companies = Field()

    directors = Field()
    scenarists = Field()
    effect_makers = Field()
    audio_directors = Field()
    main_animators = Field()
    photo_directors = Field()
    mechanical_designers = Field()
    anime_directors = Field()
    charactor_designers = Field()
    musicians = Field()
    storyboard_directors = Field()
    acts = Field()
    desc = Field()
    episodes = Field()


class CG(BasicItem):
    django_model = models.CG

    crawled_from = Field()
    large_file_url = Field()
    file_url = Field()
    source = Field()
    site_pk = Field()

    md5 = Field()
    pixiv_id = Field()
    path = Field()

    donmai_uploader_id = Field()
    rating = Field()
    fav_count = Field()
    score = Field()

    artist_tags = Field()
    character_tags = Field()
    general_tags = Field()
    copyright_tags = Field()

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
    tags_string = Field()
    author = Field()
    source = Field()
    score = Field()
    file_ext = Field()

    file_path = Field()
    preview_path = Field()

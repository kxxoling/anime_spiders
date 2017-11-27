# -*- coding: utf-8 -*-
import os

import django

from .utils import download_file, prepare_download, save_to_django_filer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exhibition.settings")

django.setup()


class DjangoItemPipeline(object):

    def process_item(self, item, spider):
        item.save()
        return item


class CGTagsPipeline(object):

    def process_item(self, item, spider):
        general_tags = item['general_tags'].split(' ')
        artist_tags = item['general_tags'].split(' ')
        character_tags = item['character_tags'].split(' ')
        copyright_tags = item['general_tags'].split(' ')
        item.instance.general_tags.add(*general_tags)
        item.instance.artist_tags.add(*artist_tags)
        item.instance.character_tags.add(*character_tags)
        item.instance.copyright_tags.add(*copyright_tags)
        return item


class DonmaiFileDownloadPipeline(object):

    def process_item(self, item, spider):
        file_url = item['large_file_url']
        file_full_name = prepare_download(file_url, spider)

        if not os.path.exists(file_full_name):
            download_file('http://danbooru.donmai.us/' + file_url, file_full_name, spider=spider)
            save_to_django_filer('danbooru_donmai_us', file_full_name, item.instance, 'file')

        item.instance.path = file_full_name.lstrip('.storage/')
        return item


class DaviantArtFileDownloadPipeline(object):

    def process_item(self, item, spider):
        file_url = item['large_file_url']
        domain = item['source'].split('/')[2]
        file_full_name = prepare_download(file_url, spider, file_dir=domain.replace('.', '_'))
        if not os.path.exists(file_full_name):
            download_file(file_url, file_full_name)
            save_to_django_filer(domain.replace('.', '_'), file_full_name, item.instance, 'file')

        item.instance.path = file_full_name.lstrip('.storage/')
        return item


class TwitterImageDownloadPipeline(object):

    def process_item(self, item, spider):
        file_url = item['large_file_url']
        sub_folder, twitter_pk = item['path'].rsplit('_', 1)
        ext = file_url.rsplit('.', 1)[-1]
        folder_full_path = os.path.join('.storage/', 'twitter_com', sub_folder)
        if not os.path.exists(folder_full_path):
            os.makedirs(folder_full_path)
        file_full_name = os.path.join(folder_full_path, '%s.%s' % (twitter_pk, ext))
        if not os.path.exists(file_full_name):
            download_file(file_url, file_full_name)
            save_to_django_filer('twitter_com', file_full_name, item.instance, 'file')

        item.instance.path = file_full_name.lstrip('.storage/')
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
            download_file(cover_url, file_full_name)
            save_to_django_filer('bangumi_tv', file_full_name, item.instance, 'cover_file')
        item['cover_path'] = file_full_name.lstrip('.storage/')
        return item


class TorrentDownloadPipeline(object):

    def process_item(self, item, spider):
        if not item['torrent']:
            return item

        torrent_url = spider.get_full_url(item['torrent'])
        # torrent_url = item['torrent']
        file_full_name = prepare_download(torrent_url, spider)
        if os.path.exists(file_full_name):
            return item
        download_file(torrent_url, file_full_name)
        # TODO: Save file to django filer
        item['torrent_path'] = file_full_name.lstrip('.storage/')
        return item


class ShortVideoDownloadPipeline(object):

    def process_item(self, item, spider):
        if item['file_url']:
            file_full_name = prepare_download(item['file_url'], spider)
            if not os.path.exists(file_full_name):
                download_file(item['file_url'], file_full_name, spider=spider)
                # TODO: Save file to django filer
            item['file_path'] = file_full_name.lstrip('.storage/')

        if item['preview_url']:
            file_full_name = prepare_download(item['preview_url'], spider)
            if not os.path.exists(file_full_name):
                download_file(item['preview_url'], file_full_name)
                save_to_django_filer('sakuga', file_full_name, item.instance, 'preview')

            item['preview_path'] = file_full_name.lstrip('.storage/')
        return item


class EHImageDownloadPipeline(object):

    def process_item(self, item, spider):
        image_url = item['url']
        file_name = image_url.rsplit('/', 1)[-1]
        file_dir = os.path.join('.storage', item['dir'])
        file_full_name = os.path.join(file_dir, file_name)
        if os.path.exists(file_full_name):
            return item
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        download_file(image_url, file_full_name)
        return item


class PixivDownloadPipeline(object):

    def process_item(self, item, spider):
        file_full_name = prepare_download(item['large_file_url'])
        download_file(
            item['large_file_url'], file_full_name, headers={
                'Referer': 'https://www.pixiv.net/'
            }
        )
        save_to_django_filer('pixiv_net', file_full_name, item.instance, 'file')
        return item

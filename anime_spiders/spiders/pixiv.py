# -*- coding: utf-8 -*-
import re

from scrapy import Spider
import requests

from anime_spiders.items import CG


class PixivIllustSpider(Spider):
    name = 'pixiv_illust'
    allowed_domains = ['pixiv.net']
    start_urls = [
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.PixivDownloadPipeline': 100,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        },
    }

    def parse(self, rsp):
        """ Parse CG items from pixiv illust page

        @url
        @returns items 1 200
        @scraps crawled_from site_pk large_file_url file_url source
        """
        wrapper = rsp.xpath('//div[@id="wrapper"]')
        wrapper_text = wrapper.extract()[0]
        pixiv_data = extract_pixiv_path(wrapper_text)
        pixiv_data.pop('order')
        order = 0
        while True:
            large_file_url = 'https://i.pximg.net/img-original/img/{year}/{month}/{day}/{hour}/{minute}/{second}/{pk}_p{order}.jpg'.format(order=order, **pixiv_data)
            if requests.head(large_file_url, headers={'Referer': 'https://www.pixiv.net/'}).status_code == 404:
                break
            yield CG(
                crawled_from='pixiv.net',
                site_pk=pixiv_data['pk'],
                large_file_url=large_file_url,
                file_url=large_file_url,
                source=rsp.url,
            )
            order += 1


class PixivUserFirstPageSpider(Spider):
    """ Scrape 1st page of Pixiv user
    Not recommoned to use.
    """
    name = 'pixiv_user_1p'
    allowed_domains = ['pixiv.net']
    start_urls = [
    ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.PixivDownloadPipeline': 100,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        },
    }

    def parse(self, rsp):
        """ Parse CG items from gallery page

        @url
        @returns items 1 200
        @scraps crawled_from site_pk large_file_url file_url source
        """
        preview_images = rsp.xpath('//div[@class="newindex"]//ul[contains(@class, "ui-brick")]/li//img/@src').extract()
        for image in preview_images:
            pixiv_data = extract_pixiv_path(image)
            large_file_url = 'https://i.pximg.net/img-original/img/{year}/{month}/{day}/{hour}/{minute}/{second}/{pk}_p{order}.jpg'.format(**pixiv_data)
            yield CG(
                crawled_from='pixiv.net',
                site_pk=pixiv_data['pk'],
                large_file_url=large_file_url,
                file_url=large_file_url,
                source='https://www.pixiv.net/member_illust.php?mode=medium&illust_id={pk}'.format(**pixiv_data),
            )


pixiv_ptn = re.compile(r'''
https://i.pximg.net/c/\d{3,4}x\d{3,4}.{0,4}/img-master/img/
(?P<year>\d+)/
(?P<month>\d+)/
(?P<day>\d+)/
(?P<hour>\d+)/
(?P<minute>\d+)/
(?P<second>\d+)/
(?P<pk>\d+)
_p(?P<order>\d{1,3})_
(master|square)
\d{3,5}
\.?(?P<ext> jpg|png|jpeg)
''', re.VERBOSE)


def extract_pixiv_path(square_path_wrapper):
    """
    """
    pixiv_data = pixiv_ptn.search(square_path_wrapper)
    if pixiv_data:
        return pixiv_data.groupdict()
    return None

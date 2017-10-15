# -*- coding: utf-8 -*-
from scrapy import Spider, Request

# from scrapy.contrib.spiders.init import InitSpider


class EHGallerySpider(Spider):
    name = 'eh_gallery'
    allowed_domains = ['e-hentai.org']
    start_urls = []

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.EHImageDownloadPipeline': 100,
        }
    }

    def parse(self, rsp):
        """ Parse pages from page
        @url
        @returns requests 1
        """
        dir_name = rsp.xpath('//h1[@id="gj"]/text()').extract_first() or \
            rsp.xpath('//h1[@id="gn"]/text()').extract_first()
        for request in self.parse_page(rsp, dir_name):
            yield request
        pages_set = set(rsp.xpath('//table[@class="ptb"]//td/a/@href').extract())
        pages_set.remove(rsp.url)
        pages = list(pages_set)
        for page in pages:
            yield Request(page, callback=self.parse_page, meta={'dir': dir_name})

    def parse_page(self, rsp, dir_name=None):
        """ Parse images from page
        @url
        @returns requests 1 100
        """
        image_pages = rsp.xpath('//div[@class="gdtm"]//a/@href').extract()
        for image_page in image_pages:
            yield Request(
                image_page,
                callback=self.parse_image_page,
                meta={'dir': dir_name or rsp.meta['dir']}
            )

    def parse_image_page(self, rsp):
        """ Parse image dict from page

        @url
        @returns items 1
        @scraps dir url
        """
        return {
            'dir': rsp.meta['dir'],
            'url': rsp.xpath('//img[@id="img"]/@src').extract_first(),
        }

    def get_full_url(self, url):
        return url


class ExGallerySpider(EHGallerySpider):
    name = 'ex_gallery'
    allowed_domains = ['exhentai.org']
    start_urls = ['']

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.EHImageDownloadPipeline': 100,
        }
    }
    dir_name = None

    def make_requests_from_url(self, url):
        cookies = {'ipb_member_id': '', 'ipb_pass_hash': '', 'ipb_session_id': ''}
        return Request(url, dont_filter=True, cookies=cookies)

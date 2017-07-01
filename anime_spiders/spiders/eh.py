# -*- coding: utf-8 -*-
from scrapy import Spider, Request
# from scrapy.contrib.spiders.init import InitSpider


class EHGallerySpider(Spider):
    name = 'eh_gallery'
    allowed_domains = ['e-hentai.org']
    start_urls = [
        'https://e-hentai.org/g/608036/a3b4c123dd/',
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.EHImageDownloadPipeline': 100,
        }
    }
    dir_name = None

    def parse(self, rsp):
        self.dir_name = rsp.xpath('//h1[@id="gj"]/text()').extract_first() or \
            rsp.xpath('//h1[@id="gn"]/text()').extract_first()
        for item in self.parse_page(rsp):
            yield item
        pages_set = set(rsp.xpath('//table[@class="ptb"]//td/a/@href').extract())
        pages_set.remove(rsp.url)
        pages = list(pages_set)
        for page in pages:
            yield Request(page, callback=self.parse_page)

    def parse_page(self, rsp):
        image_pages = rsp.xpath('//div[@class="gdtm"]//a/@href').extract()
        for image_page in image_pages:
            yield Request(image_page, callback=self.parse_image_page)

    def parse_image_page(self, rsp):
        return {
            'dir': self.dir_name,
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
        cookies = {
            'ipb_member_id': '',
            'ipb_pass_hash': '',
            'ipb_session_id': ''
        }
        return Request(url, dont_filter=True, cookies=cookies)

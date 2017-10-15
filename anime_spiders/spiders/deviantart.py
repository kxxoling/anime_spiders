# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest, Request

from anime_spiders.items import CG

import re
import json


class DeviantartGallerySpider(scrapy.Spider):
    name = "da_gallery"
    allowed_domains = ["deviantart.com"]
    start_urls = ['']
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.DaviantArtFileDownloadPipeline': 150,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        }
    }

    def make_requests_from_url(self, url):
        request = super(DeviantartGallerySpider, self).make_requests_from_url(url)
        request.cookies['userinfo'] = self.userinfo
        return request

    def parse(self, rsp):
        """ Parse CG items from gallery page

        @url
        @returns items 1 40
        @scraps crawled_from site site_pk large_file_url file_url source
        """
        arts = rsp.xpath('//span[@class="thumb wide"]/a[@class="torpedo-thumb-link"]/@href'
                         ).extract()
        for art in arts:
            yield Request(art, callback=self.parse_image)

        csrf = re.findall(r'"csrf":"(.*?)"', rsp.text)[0]
        gallery_id = rsp.url.split('/')[4]
        username = rsp.url.split('/')[2].split('.')[0]
        for cg in [
            FormRequest(
                'http://www.deviantart.com/dapi/v1/gallery/' + gallery_id + '?iid=0&mp=1',
                formdata=dict(username=username, offset='24', limit='24', _csrf=csrf, dapiIid='0'),
                callback=self.parse_json
            )
        ]:
            yield cg

    def parse_json(self, rsp):
        """ Parse CG items from JSON response
        @url
        @returns items 1 40
        @scraps crawled_from site site_pk large_file_url file_url source
        """
        data = json.loads(rsp.text)
        # has_more = data['content']['has_more']
        arts = data['content']['results']
        for art in arts:
            yield self.parse_json_result(art['html'])

    def parse_image(self, rsp):
        """ Parse CG items from image page
        @url
        @returns items 1
        @scraps crawled_from site site_pk large_file_url file_url source
        """
        url = rsp.url
        site_pk = url.split('/')[4].split('-')[-1]
        file_url = large_file_url = rsp.xpath('//img[@class="dev-content-full "]/@src')\
                                       .extract_first()
        return CG(
            crawled_from='deviantart.com',
            site_pk=site_pk,
            large_file_url=large_file_url,
            file_url=file_url,
            source=url,
        )

    def parse_json_result(self, art):
        try:
            file_url = large_file_url = re.findall(r'data-super-full-img="(.*?)"', art)[0]
        except IndexError:
            return None
        url = re.findall(r'href="(.*?)"', art)[0]
        site_pk = url.split('/')[4].split('-')[-1]
        return CG(
            crawled_from='deviantart.com',
            site_pk=site_pk,
            large_file_url=large_file_url,
            file_url=file_url,
            source=url,
        )

    def get_full_url(self, url):
        return url

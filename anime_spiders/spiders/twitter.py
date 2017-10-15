# -*- coding: utf-8 -*-
import scrapy

from anime_spiders.items import CG


class TwitterPostSpider(scrapy.Spider):
    name = "twitter_post"
    allowed_domains = ["twtter.com"]
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.TwitterImageDownloadPipeline': 150,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        }
    }

    def parse(self, rsp):
        """ Parse images from post

        @url
        @returns items 1 20
        @scraps username url
        """

        username = rsp.url.split('/')[3]
        images = rsp.xpath(
            '//div[@class="permalink-inner permalink-tweet-container"]'
            '//div[@class="AdaptiveMediaOuterContainer"]'
            '//img/@src'
        ).extract()
        # text = rsp.xpath('//div[@class="permalink-inner permalink-tweet-container"]'
        #                  '//p[contains(@class, "tweet-text")]/text()').extract_first()
        twitter_pk = int(rsp.url.split('/')[-1])
        for image in images:
            yield CG(
                crawled_from='twitter.com',
                large_file_url=image,
                file_url=image,
                source=rsp.url,
                site_pk=twitter_pk,
                path='%s_%s' % (username, twitter_pk),
            )

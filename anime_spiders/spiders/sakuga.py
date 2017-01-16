# coding: utf-8
from urllib import urlencode
from urlparse import urlparse, parse_qs

from scrapy import Spider, Request


class SakugaSpider(Spider):
    name = 'sakuga'
    start_urls = [
        'https://sakugabooru.com/post.xml?page=1',
    ]
    base_url = 'https://sakugabooru.com/post.xml'

    def parse(self, rsp):
        posts = rsp.xpath('//posts/post')
        if not posts:
            return
        for p in posts:
            yield dict(
                id=int(p.xpath('@id').extract_first()),
                md5=p.xpath('@md5').extract_first(),
                preview_url=p.xpath('@preview_url').extract_first(),
                file_url=p.xpath('@file_url').extract_first(),
                file_size=int(p.xpath('@file_size').extract_first()),
                tags=p.xpath('@tags').extract_first(),
                author=p.xpath('@author').extract_first(),
                source=p.xpath('@source').extract_first(),
                score=int(p.xpath('@score').extract_first()),
                file_ext=p.xpath('@file_ext').extract_first(),
            )

        next_url = self.get_next_url(rsp)
        yield Request(next_url, callback=self.parse)

    def get_next_url(self, rsp):
        current_url = rsp.url
        parsed_url = urlparse(current_url)
        args = parse_qs(parsed_url.query)
        args['page'] = int(args['page'][0]) + 1
        next_url = '{}?{}'.format(self.base_url, urlencode(args))
        return next_url

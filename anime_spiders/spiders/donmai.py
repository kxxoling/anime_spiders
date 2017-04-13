# coding: utf-8
from urlparse import urlparse, parse_qs
from urllib import urlencode
import datetime

from scrapy import Spider, Request

from anime_spiders.items import CG


class DonmaiHotSpider(Spider):
    name = 'donmai_hot'
    start_urls = [
        'http://danbooru.donmai.us/posts.xml?page=1&tags=order%3Arank',
    ]
    base_url = 'http://danbooru.donmai.us/posts.xml'
    tags = 'order:rank'

    def parse(self, rsp):
        posts = rsp.xpath('//posts/post')
        if not posts:
            return
        for p in posts:
            yield CG(
                large_file_url=p.xpath(
                    'large-file-url/text()').extract_first(),
                file_url=p.xpath('file-url/text()').extract_first(),
                source=p.xpath('source/text()').extract_first(),
                id=int(p.xpath('id/text()').extract_first()),
                tags_string=p.xpath('tag-string/text()').extract_first(),
                md5=p.xpath('md5/text()').extract_first(),
                pixiv_id=p.xpath('pixiv-id/text()').extract_first(),
            )

        next_url = self.get_next_url(rsp)
        yield Request(next_url, callback=self.parse)

    def get_next_url(self, rsp):
        current_url = rsp.url
        parsed_url = urlparse(current_url)
        args = parse_qs(parsed_url.query)
        new_args = {}
        new_args['page'] = int(args['page'][0]) + 1
        new_args['tags'] = self.tags
        next_url = '{}?{}'.format(self.base_url, urlencode(new_args))
        return next_url


class DonmaiMonthlyPopilarSpider(Spider):
    name = 'donmai_monthly_pop'
    start_urls = [
        'http://danbooru.donmai.us/explore/posts/popular.xml'
        '?date=%s&scale=month' % datetime.datetime.now().date().isoformat(),
    ]
    base_url = 'http://danbooru.donmai.us/posts.xml'

    def parse(self, rsp):
        for p in rsp.xpath('//posts/post'):
            yield CG(
                large_file_url=p.xpath(
                    'large-file-url/text()').extract_first(),
                file_url=p.xpath('file-url/text()').extract_first(),
                source=p.xpath('source/text()').extract_first(),
                id=int(p.xpath('id/text()').extract_first()),
                tags_string=p.xpath('tag-string/text()').extract_first(),
                md5=p.xpath('md5/text()').extract_first(),
                pixiv_id=p.xpath('pixiv-id/text()').extract_first(),
            )

        next_url = self.get_next_url(rsp)
        yield Request(next_url, callback=self.parse)

    def get_next_url(self, rsp):
        current_url = rsp.url
        parsed_url = urlparse(current_url)
        args = parse_qs(parsed_url.query)
        new_args = {}
        date = datetime.datetime.strptime(args['date'][0], '%Y-%m-%d')
        if date.month == 1:
            prev_month = '{}-{}-{}'.format(date.year-1, 12, date.day)
        else:
            prev_month = '{}-{}-{}'.format(
                date.year, date.month-1, date.day)
        new_args['date'] = prev_month
        next_url = '{}?{}'.format(self.base_url, urlencode(new_args))
        return next_url

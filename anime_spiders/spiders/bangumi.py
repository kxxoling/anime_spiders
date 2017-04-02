# coding: utf-8
from urllib import urlencode
from urlparse import urlparse, parse_qs

from scrapy import Spider, Request


class BangumiSpider(Spider):
    name = 'bangumi'
    start_urls = [
        'http://bangumi.tv/anime/browser/?sort=date&page=1',
    ]
    base_url = 'http://bangumi.tv/anime/browser/'

    def parse(self, rsp):
        subjects = rsp.xpath('//ul[@id="browserItemList"]/li')
        if not subjects:
            return
        for s in subjects:
            link = s.xpath('a/@href').extract_first()
            subject_id = int(link.replace('/subject/', ''))
            yield dict(
                id=subject_id,
                link=link,
                cover=s.xpath('a/span/img[@class="cover"]/@src')
                       .extract_first(),
                name=s.xpath('div[@class="inner"]/h3/a/text()')
                       .extract_first(),
                orig_name=s.xpath('div[@class="inner"]/h3/small/text()')
                           .extract_first(),
                pub_date=s.xpath('div[@class="inner"]/p/text()')
                          .extract_first()
                          .strip(),
            )

        next_url = self.get_next_url(rsp)
        yield Request(next_url, callback=self.parse)

    def get_next_url(self, rsp):
        current_url = rsp.url
        parsed_url = urlparse(current_url)
        args = parse_qs(parsed_url.query)
        page = int(args['page'][0]) + 1
        next_url = '{}?{}'.format(self.base_url,
                                  urlencode(dict(sort='date', page=page)))
        return next_url

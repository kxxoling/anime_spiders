# coding: utf-8
from scrapy import Spider


class DmhyRssSpider(Spider):
    name = 'dmhy_rss'
    start_urls = [
        'https://share.dmhy.org/topics/rss/rss.xml',
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }

    def parse(self, rsp):
        items = rsp.xpath('//rss/channel/item')
        if not items:
            return
        for i in items:
            yield dict(
                title=i.xpath('title/text()').extract_first(),
                link=i.xpath('link/text()').extract_first(),
                pub_date=i.xpath('pubDate/text()').extract_first(),
                description=i.xpath('description/text()').extract_first(),
                magnet=i.xpath('enclosure/@url').extract_first(),
                author=i.xpath('author/text()').extract_first(),
                category=i.xpath('category/text()').extract_first(),
            )

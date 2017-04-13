# coding: utf-8
from scrapy import Spider
import dateutil.parser

from anime_spiders.items import Torrent


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
            item = Torrent(
                crawled_from='share.dmhy.org',
                site_pk=int(i.xpath('link/text()').extract_first()
                    .replace('http://share.dmhy.org/topics/view/', '')
                    .split('_', 1)[0]
                ),
                title=i.xpath('title/text()').extract_first(),
                link=i.xpath('link/text()').extract_first(),
                pub_date=dateutil.parser.parse(
                    i.xpath('pubDate/text()').extract_first()),
                # description=i.xpath('description/text()').extract_first(),
                magnet=i.xpath('enclosure/@url').extract_first(),
                author=i.xpath('author/text()').extract_first(),
                category=i.xpath('category/text()').extract_first(),
                torrent=None,
            )
            yield item

    def get_full_url(self, url):
        return url

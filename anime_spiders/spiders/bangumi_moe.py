# coding: utf-8
from scrapy.spiders import XMLFeedSpider
import dateutil.parser
import time

from anime_spiders.items import Torrent


class BangumiMoeFeedSpider(XMLFeedSpider):
    name = 'bangumi_moe'
    start_urls = [
        'https://bangumi.moe/rss/latest',
    ]
    itertag = 'item'
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }

    def parse_node(self, rsp, node):
        item = Torrent()
        item['crawled_from'] = 'bangumi.moe'
        item['site'] = 'bangumi_moe'
        item['site_pk'] = node.xpath('guid/text()').extract_first()\
                              .replace('https://bangumi.moe/torrent/', '')
        item['title'] = node.xpath('title/text()').extract_first()
        try:
            item['team_name'] = item['title'].split(u'【')[1].split(u'】')[0]
        except IndexError:
            item['team_name'] = item['title'].split(u'[')[1].split(u']')[0]
        item['torrent'] = node.xpath('enclosure/@url').extract_first()
        item['link'] = node.xpath('link/text()').extract_first()
        item['pub_date'] = dateutil.parser.parse(
            node.xpath('pubDate/text()').extract_first()
        )
        item['site_pk'] = time.mktime(item['pub_date'].timetuple())
        try:
            item['category'] = item['title'].split('(')[-1].split(')')[0]
        except IndexError:
            pass    # noqa
        item['category'] = item['title'].split('(')[-1].split(')')[0]
        return item

    def get_full_url(self, url):
        return url

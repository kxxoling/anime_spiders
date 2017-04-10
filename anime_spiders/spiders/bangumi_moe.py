# coding: utf-8
from scrapy.spiders import XMLFeedSpider

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
        item['site'] = 'bangumi_moe'
        item['id'] = node.xpath('guid/text()').extract_first()\
                         .replace('https://bangumi.moe/torrent/', '')
        item['title'] = node.xpath('title/text()').extract_first()
        try:
            item['team_name'] = item['title'].split(u'【')[1].split(u'】')[0]
        except IndexError:
            item['team_name'] = item['title'].split(u'[')[1].split(u']')[0]
        item['torrent'] = node.xpath('enclosure/@url').extract_first()
        item['link'] = node.xpath('link/text()').extract_first()
        item['pub_date'] = node.xpath('pubDate/text()').extract_first()
        try:
            item['category'] = item['title'].split('(')[-1].split(')')[0]
        except IndexError:
            pass    # noqa
        item['category'] = item['title'].split('(')[-1].split(')')[0]
        return item

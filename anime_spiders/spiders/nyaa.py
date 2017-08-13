# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import Spider, XMLFeedSpider
import dateutil.parser

from anime_spiders.items import Torrent


class NyaaRSSSpider(XMLFeedSpider):
    name = 'nyaa_rss'
    start_urls = [
        'https://nyaa.si/?page=rss',
    ]
    itertag = 'item'

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.TorrentDownloadPipeline': 100,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        },
    }

    def parse_node(self, rsp, node):
        """ Parse torrent item from feed

        @url https://nyaa.si/?page=rss
        @returns items 10 100
        @scraps crawled_from site_pk site title torrent link
            pub_date
        """
        item = Torrent()
        item['crawled_from'] = 'nyaa.si'
        item['site'] = 'nyaa_si'
        item['title'] = node.xpath('title/text()').extract_first()
        item['torrent'] = node.xpath('link/text()').extract_first().replace('https://nyaa.si', '')
        item['link'] = item['torrent'].replace('/torrent', ''),
        item['site_pk'] = int(node.xpath('guid/text()')
                              .extract_first().rsplit('/', 1)[-1])
        item['pub_date'] = dateutil.parser.parse(
            node.xpath('pubDate/text()').extract_first())
        return item

    def get_full_url(self, url):
        return 'https://nyaa.si%s' % url


class NyaaSpider(Spider):
    name = 'nyaa'
    start_urls = [
        'https://nyaa.si/',
    ]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.TorrentDownloadPipeline': 100,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        },
    }

    def parse(self, rsp):
        """ Parse torrent items from page

        @url https://acg.rip/page/1
        @returns items 1 30
        @scraps topic_id title size magnet link pub_date
            torrent magnet crawled_from site site_pk
        """
        torrent_nodes = rsp.xpath(
            "//div[@class='table-responsive']/table/tbody/tr")
        for i in torrent_nodes:
            item = Torrent()
            item['crawled_from'] = 'nyaa.si'
            item['site'] = 'nyaa_si'
            item['category'] = i.xpath('td')[0].xpath('a/@href').extract_first().replace('/?c=', '')

            item['title'] = i.xpath('td')[1].xpath('a/text()').extract_first()

            item['link'] = i.xpath('td')[1].xpath('a/@href').extract_first()
            item['site_pk'] = int(item['link'].replace('/view/', '').replace('#comments', ''))

            links = i.xpath('td')[2].xpath('a/@href')
            for link in links:
                link = link.extract()
                if link.startswith('magnet'):
                    item['magnet'] = link
                elif link.startswith('/'):
                    item['torrent'] = link

            size = i.xpath('td')[3].xpath('text()').extract_first()
            if 'MiB' in size:
                size_num = float(size.replace(' MiB', ''))
            elif 'GiB' in size:
                size_num = float(size.replace(' GiB', '')) * 1024
            item['size'] = size_num

            item['pub_date'] = dateutil.parser.parse(
                i.xpath('td')[4].xpath('text()').extract_first())
            yield item
        next_page = rsp.xpath(u'//center/nav/'
                              u'ul[@class="pagination"]/li/'
                              u'a[text()="»"]').xpath('@href').extract_first()
        next_page = self.get_full_url(next_page)
        yield Request(next_page, callback=self.parse)

    def get_full_url(self, url):
        return 'https://nyaa.si%s' % url

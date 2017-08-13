# coding: utf-8
from scrapy import Spider, Request
from anime_spiders.items import Torrent


class AcgRipSpider(Spider):
    name = 'acg_rip'
    start_urls = [
        'https://acg.rip/page/1',
    ]
    base_url = 'https://acg.rip/'

    custom_settings = {
        'ITEM_PIPELINES': {
            'anime_spiders.pipelines.TorrentDownloadPipeline': 100,
            'anime_spiders.pipelines.DjangoItemPipeline': 200,
        },
    }

    def parse(self, rsp):
        """ Parse torrent items from page

        @url https://acg.rip/page/1
        @returns items 1 30
        @scraps team_title team_name team_link team_id topic_id title size
            torrent crawled_from
        """
        items = rsp.xpath('//table/tr')
        if not items:
            return
        for i in items:
            # auth_date = i.xpath("td[starts-with(@class,'date ')]")[0]
            # author_name = auth_date.xpath('div/a/text()').extract_first()
            # author_id = int(auth_date.xpath('div/a/@href')
            #                 .extract_first().replace('/user/', ''))
            team_title = i.xpath("td[@class='title']")[0]
            team_name = team_title.xpath('span[contains(@class,"label-team")]'
                                         '/a/text()').extract_first()
            team_link = team_title.xpath(
                'span[contains(@class,"label-team")]/a/@href').extract_first()
            team_id = int(team_link.replace('/team/', '')) \
                if team_link else None
            topic_id = int(team_title
                           .xpath('span[@class="title"]/a/@href')
                           .extract_first().replace('/t/', ''))
            title = team_title.xpath('span[@class="title"]/a/text()') \
                              .extract_first()
            size = i.xpath("td[@class='size']/text()").extract_first()
            if 'MB' in size:
                size_num = float(size.replace(' MB', ''))
            elif 'GB' in size:
                size_num = float(size.replace(' GB', '')) * 1024

            yield Torrent(
                crawled_from='acg.rip',
                site_pk=topic_id,
                title=title,
                team_name=team_name,
                team_id=team_id,
                size=size_num,
                torrent=i.xpath("td[@class='action']/a/@href").extract_first()
            )

        next_url = self.get_next_url(rsp)
        yield Request(next_url, callback=self.parse)

    def get_next_url(self, rsp):
        current_url = rsp.url
        page = int(current_url.replace('https://acg.rip/page/', ''))
        next_url = '{}page/{}'.format(self.base_url, page+1)
        return next_url

    def get_full_url(self, url):
        return u'https://acg.rip%s' % url

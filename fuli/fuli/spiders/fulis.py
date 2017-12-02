# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class FulisSpider(CrawlSpider):
    name = 'fulis'
    allowed_domains = ['0855vod.com']
    start_urls = ['http://0855vod.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/xianzhiji/index-2.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        movie_name = response.xpath('//span[@class="sTit"]/text()').extract()[0]
        print(movie_name)

        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

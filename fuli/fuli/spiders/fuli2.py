# -*- coding: utf-8 -*-
import scrapy
from fuli.items import FuliItem


class Fuli2Spider(scrapy.Spider):
    name = 'fuli2'
    allowed_domains = ['0855.com']
    start_urls = []

    for page in range(1,80):
        base_url = 'http://www.0855vod.com/f/xianzhiji/index-%d.html' %page
        start_urls.append(base_url)

    def parse(self, response):
        item = FuliItem()

        url = 'http://0855vod.com'
        proxy_list = response.xpath('//ul[@class="List clearfix"]')
        for proxy in proxy_list:
            movie_list = proxy.xpath('.//span[@class="sTit"]/text()').extract()
            for movie_name in movie_list:
               print(movie_name)
            link_list = response.xpath('.//div[@class="pic"]//a/@href').extract()
            for movie_link in link_list:
                movie_links = url + movie_link
                num = list(movie_links.replace('v','x') + '-1-1.html')
                num[11] = 'v'
                del num[-10]
                nums = ''.join(num)
                print(nums)

            item['movie_name'] = movie_name
            item['nums'] = nums

            yield item


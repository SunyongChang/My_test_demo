# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class FuliPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonPipeline(object):
    def process_item(self, item, spiser):
        self.f.write(json.dumps(dict(item),ensure_ascii = False) + '\n')

        return item

    def close_spider(self,spider):
        self.f.close()
class MyfuliPipeline(JsonPipeline):
    def __init__(self):
        self.f = open('fuli.json','w',encoding = 'utf-8')

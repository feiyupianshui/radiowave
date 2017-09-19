#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
from scrapy.spider import CrawlSpider, Rule, Request #偷懒爬全站
from scrapy.linkextractors import LinkExtractor #抽出链接对象
from scrapy import FromRequest #登录包
from huaban.items import HuabanItem

class myspider(CrawlSpider):
    name = 'dianbo'
    allowed_domain = ['http://dbfansub.com/']
    start_url = ['http://dbfansub.com/']

    rules = (
        Rule(LinkExtractor(allow=('')), callback = 'parse_item', follow=True),
    )
    #
    def parse_item(self,reponse):
        print(response.url)
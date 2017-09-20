#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
from scrapy.spider import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FormRequest
from radiowave.items import RadiowaveItem

class myspider(CrawlSpider):
    name = 'radiowave'
    allowed_domain = ['dbfansub.com']
    start_url = ['http://dbfansub.com/']

    rules = (
        Rule(LinkExtractor(allow=('\.html')), callback = 'parse_item', follow=True),
        # Rule(LinkExtractor(allow=('/categoty/[a-z]+/')))
    )
    def parse_item(self,reponse):
        print(response.url)
        pass
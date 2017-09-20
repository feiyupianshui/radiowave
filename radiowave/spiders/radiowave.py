#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
import re
from scrapy.spider import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
# from scrapy import FormRequest
from bs4 import BeautifulSoup
from radiowave.items import RadiowaveItem

class myspider(CrawlSpider):
    name = 'radiowave'
    allowed_domain = ['dbfansub.com']
    start_urls = ['http://dbfansub.com/']

    rules = (
        Rule(LinkExtractor(allow=('\.html',), deny =('weibo','qq','redirect','login',)), callback = 'parse_item', follow=True),
        #放行可用链接
    )
    def parse_item(self,response):
        # print(response.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pans = soup.find_all('a', href=re.compile("baidu"))
        for a in pans:
            panurl = a['href']
# 提取名字和集数的链接：
# <h1 class="entry-title h3" itemprop="name">【动画】瑞克与莫蒂 Rick and Morty 第三季(更新至08集) 电波字幕组</h1>
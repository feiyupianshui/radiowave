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
        name = soup.find('h1', class_="entry-title h3").get_text()
        category = name[:4].split('【')[1].split('】')[0]
        str = '【' + category + '】'
        item['dramaname'] = name.split('电波字幕组')[0].split(str)[1]
        item['category'] = category
        item['imgurl'] = soup.find('div', class_="article_index").next_sibling.li.a['href']

        pans = soup.find_all('a', href=re.compile("baidu"))
        for a in pans:
            item['dramaurl'] = a['href']

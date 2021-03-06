#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
import re
from ..mysqlpipelines.sql import Sql
from scrapy.spider import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FormRequest
from bs4 import BeautifulSoup
from radiowave.items import RadiowaveItem

# account = 'Q8B1948D90565EAA8F705E7C91E4CAAE6'
# password = '^118667'

class myspider(CrawlSpider):
    name = 'radiowave'
    allowed_domain = ['dbfansub.com']
    start_urls = ['http://dbfansub.com/user/login/?redirect_to=http%3A%2F%2Fdbfansub.com%2Ftvshow%2F8902.html']

    def parse_start_url(self, response):
        formdata = {
            'log': 'Q8B1948D90565EAA8F705E7C91E4CAAE6',
            'pwd': '^118667',
            'wp-submit': '登录',
            'redirect_to': 'http://dbfansub.com/tvshow/8902.html',
            'testcookie': '1'
        }
        return [FormRequest.from_response(response, formdata=formdata, callback=self.after_login)]

    def after_login(self,response):
        lnk = 'http://dbfansub.com/'
        return Request(lnk)

    rules = (
        Rule(LinkExtractor(allow=('\.html',), deny =('weibo','qq','redirect','login',)), callback = 'parse_item', follow=True),
        #放行可用链接
    )

    def parse_item(self,response):
        item = RadiowaveItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', class_="entry-title h3").get_text()
        category1 = name[:4]
        category2 = category1.split('【')[1]
        category3 = category2.split('】')[0]
        str = '【' + category3 + '】'
        dramaname = name.split('电波字幕组')[0].split(str)[1]
        dramaid = response.url.split('.html')[0].split('/')[-1]
        item['dramaname'] = name.split('电波字幕组')[0].split(str)[1]
        item['category'] = category3
        item['dramaid'] = response.url.split('.html')[0].split('/')[-1]
        item['imgurl'] = soup.find('div', class_="article_index").next_sibling.li.a['href']

        pans = soup.find_all('a', href=re.compile("baidu"))
        for a in pans:
            item['dramaurl'] = a['href']

        return item

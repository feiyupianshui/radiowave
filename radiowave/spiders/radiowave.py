#!/use/bin/env python
#_*_coding:utf-8_*_
import scrapy
import re
# from ..mysqlpipelines.sql import Sql
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
    dramaurls = []
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

    def parse_item(self,response):#这里千万不能用parse做函数名
        item = RadiowaveItem()
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find('h1', class_="entry-title h3").get_text()
        category = response.url.split('/')[-2]  # 这个是英文的
        dramaname = name.split('电波字幕组')[0]#.split(str)[1]
        dramaid = response.url.split('.html')[0].split('/')[-1]
        item['dramaname'] = dramaname
        item['category'] = category
        item['dramaid'] = response.url.split('.html')[0].split('/')[-1]
        imgurltag = soup.find('img', class_="alignnone")
        if imgurltag is None:
            print('图片不存在')
            item['imgurl'] = '图片不存在'
        else:
            item['imgurl'] = imgurltag['src']
        # item['dramapage'] = response.url
        # item['dramaurl'] = response.xpath('//*[@id="content"]/div[1]/div[1]/div[2]/p[a="百度云盘" or a="百度网盘"]/a[1]/@href')
        # 网页不规范，xpath根本跑不动

        dramaurls = soup.find_all('a', href=re.compile("baidu"))
        for a in dramaurls:
            dramaurl = a['href']
            self.dramaurls.append(dramaurl)
        item['dramaurl'] = self.dramaurls
        yield item


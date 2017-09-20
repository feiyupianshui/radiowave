# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RadiowaveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #下载链接
    url = scrapy.Field()
    #片名
    dramaname = scrapy.Field()
    #集数
    num = scrapy.Field()

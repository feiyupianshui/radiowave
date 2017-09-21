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
    dramaurl = scrapy.Field()
    #片名
    dramaname = scrapy.Field()
    #种类
    category = scrapy.Field()
    #海报
    imgurl = scrapy.Field()

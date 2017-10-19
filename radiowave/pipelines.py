# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import re

class RadiowavePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        # :param request: 每一个图片下载管道请求
        # :param response:
        # :param info:
        # :param strip :清洗Windows系统的文件夹非法字符，避免无法创建目录
        # :return: 每套图的分类目录
        item = request.meta['item']
        folder = 'radiowave'
        image_guid = item['dramaid']
        image_strip = image_guid.strip()#参数为空时默认去除首尾的空白符空白符（包括'\n'，'\r'，'\t'，' ')
        filename = u'full/{0}/{1}'.format(folder,image_strip)
        return filename

    def get_media_requests(self, item, info):
        # :param item: spider.py中返回的item
        pass

    def item_completed(self, results,item, info):
        pass

        return item

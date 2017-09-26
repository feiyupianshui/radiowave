#!/use/bin/env python
#_*_coding:utf-8_*_
from .sql import Sql
from radiowave.items import RadiowaveItem

class RadiowavePipeline(object):

    def process_item(self, item, spider):
        pass
#!/use/bin/env python
#_*_coding:utf-8_*_
from .sql import Sql
from radiowave.items import RadiowaveItem

class RadiowavePipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, RadiowaveItem):
            dramaid = item['dramaid']
            ret = Sql.select_dramaid(dramaid)
            if ret[0] == 1:
                print('已经存在了')
            else:
                dramaname = item['dramaname']
                category = item['category']
                imgurl = item['imgurl']
                Sql.insert_drama_name(dramaid, dramaname, category, imgurl)
                print('开始储存剧名')

            rets = Sql.select_url(dramaurl)
            if rets[0] == 1:
                print('链接已存在')
            else:
                dramaurl = item['dramaurl']
                Sql.insert_baidu_url(dramaid, dramaurl)
                print('云盘储存完毕')
            return item
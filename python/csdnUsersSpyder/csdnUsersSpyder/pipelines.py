# -*- coding: utf-8 -*-
import json
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from items import CsdnusersspyderItem

class CsdnusersspyderPipeline(object):
    def __init__(self):
        pass


    def process_item(self, item, spider):
        line = json.dumps(dict(item)) +\n
        print line 
        return item

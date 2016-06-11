# -*- coding: utf-8 -*-
import json
import codecs
import html2text
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import BlogspyderItem

class BlogspyderPipeline(object):
    def __init__(self):
        self.file =self.file = codecs.open('blogitems.json', mode='wb', encoding='utf-8')
    def process_item(self, item, spider):
        #print("In pipline: item.title= %s" % item["pageTitle"])
        item["pageContent"] = html2text.html2text(''.join(item["pageContent"]))
        line = json.dumps(dict(item) )+'\n'
        self.file.write(line.decode("unicode_escape"))
        return item

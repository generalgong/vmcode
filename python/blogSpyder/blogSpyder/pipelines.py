# -*- coding: utf-8 -*-
import json
import codecs
from elasticsearch import Elasticsearch
#import jieba

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import BlogspyderItem

class BlogspyderPipeline(object):
    def __init__(self):
      
        self.itemDic = {"pageUrl":"" ,"pageID":"","pageTitle":"","pageContent":"","pageRank":"" }
        self.es = Elasticsearch("brian1")
      
    def __del__(self):
        self.file.close()
    def process_item(self, item, spider):

        self.itemDic["pageUrl"] = item["pageUrl"]
        self.itemDic["pageID"] = item["pageID"]
        self.itemDic["pageTitle"] = item["pageTitle"].encode("utf-8")
        self.itemDic["pageContent"] = item["pageContent"].encode("utf-8")

        self.es.create(index="test-index3", doc_type="csdnblog",body=self.itemDic)
      
        return item

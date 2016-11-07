# -*- coding: utf-8 -*-
import json
import codecs
from elasticsearch import Elasticsearch
import jieba
import MySQLdb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import BlogspyderItem

class BlogspyderPipeline(object):
    def __init__(self):
      
        self.itemDic = {"pageUrl":"" ,"pageID":"","pageTitle":"","pageContent":"","pageRank":"" }
        self.es = Elasticsearch("localhost")
        self.buffer_userName = 'userName'
        self.buffer_pageRank = -1.0
        self.default_pageRank = 0.00000001
    def __del__(self):
        self.file.close()
    def getPageRankByUsername(self ,userName):
        sql = "select _2 from pageran8  where _1 = '{0}' ".format(userName)
        con = MySQLdb.connect("brian1" , "brian","general","csdn")
        cur = con.cursor()
        try:
    		  cur.execute(sql)
    		  (results,) = cur.fetchone()
    		  return results
        except:
    		  print "fetach pageValue by name({0}) falid".format(userName)  
        finally:        
    		  if con:
    		      con.close()         
      
    def process_item(self, item, spider):
        self.itemDic["pageUrl"] = item["pageUrl"]
        self.itemDic["pageID"] = item["pageID"]
        self.itemDic["pageTitle"] = item["pageTitle"].encode("utf-8")
        self.itemDic["pageContent"] = " ".join(jieba.cut(item["pageContent"].encode("utf-8")))
        # pagerank info 
        userName = item["pageUrl"].split('/')[3]     
        if userName == self.buffer_userName:            
            self.itemDic["pageRank"] = self.buffer_pageRank
        else:
            pr = self.getPageRankByUsername(userName)           
            self.itemDic["pageRank"] =  pr if pr != ''  else self.default_pageRank
            self.buffer_userName = userName
            self.buffer_pageRank = pr       

        self.es.create(index="blog", doc_type="csdn",body=self.itemDic)
        return item

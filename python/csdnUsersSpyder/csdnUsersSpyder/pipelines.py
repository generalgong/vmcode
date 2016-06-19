# -*- coding: utf-8 -*-
import json
import MySQLdb
from scrapy import signals
from scrapy.xlib.pydispatch import dispatcher

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



from items import CsdnusersspyderItem

class CsdnusersspyderPipeline(object):
    def __init__(self):
        try:
            print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n\n\n"
            self.con = MySQLdb.connect("brian1" , "brian","general","csdn")
            dispatcher.connect(self.spider_closed, signals.spider_closed)
            print("Opne connection\n")
        except:
            print "***************\n"
            if self.con:
                self.con.close()
                return 

    def process_item(self, item, spider):
        cur = self.con.cursor()
        sql = "INSERT INTO BlogUser(pageID, pageMD5,pageUrl, userName, follows ,befollowed , followNum ,befollowedNum)   VALUES ('%s', '%s' ,'%s' ,'%s','%s','%s','%s','%s')" % (item["pageID"],item["pageMD5"] , item["pageUrl"] , item["userName"],','.join(item["follow"]),','.join(item["befollowed"]),item["followNum"],item["befollowedNum"])
        print sql + "\n"
        try:
           cur.execute(sql)
           print "Insert db"
           self.con.commit()
        except:
            self.con.rollback()
        return item
    def spider_closed(self, spider, reason):
        if self.con: 
            self.con.close

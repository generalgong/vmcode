# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BlogspyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pageUrl = scrapy.Field()#页面自己的URL
    pageID  = scrapy.Field()#页面ID，
    pageMD5 = scrapy.Field()#根据页面URL计算出MD5
    pageTitle=scrapy.Field()#title
    pageContent=scrapy.Field()#提取body中的内容
    pagePubDate=scrapy.Field()#页面发布日期
    pageRank  =scrapy.Field()#pageRank value
    outLinks = scrapy.Field()
    pass

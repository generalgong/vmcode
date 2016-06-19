# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CsdnusersspyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pageUrl = scrapy.Field()#页面自己的URL
    pageID  = scrapy.Field()#页面ID，
    pageMD5 = scrapy.Field()#根据页面URL计算出MD5
    userName = scrapy.Field()
    follow  = scrapy.Field()
    followNum  = scrapy.Field()
    befollowed = scrapy.Field() ###
    befollowedNum = scrapy.Field() ###
    rencentView = scrapy.Field()
    pass

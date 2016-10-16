# -*- coding:utf-8 -*-  
#from scrapy.spiders import Spider  
from scrapy import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from GetMD5 import GetMD5
from blogSpyder.items import BlogspyderItem 
from GetUseHomePageList import GetUseHomePage
from  html2text import html2text
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
class BlogSpider(Spider):  
    def __init__(self):
        self.pageNumber =0
        self.homePages = GetUseHomePage()

  
    name = "csdnBlogSpyder"  
    #减慢爬取速度 为5s  
    download_delay = 2 
    allowed_domains = ["blog.csdn.net" , "my.csdn.net"] 
    
    start_urls = [  
        "http://my.csdn.net/service/main/get_user_contribute?type=blog&username=brian_gong"
    ]  
            
    def parse(self, response):          
        jdata = json.loads(response.body)
        articleId = jdata['result'][0]['ArticleId']
        userName = jdata['result'][0]['UserName']       
        articleUrl = "http://blog.csdn.net/%s/article/details/%s" % (userName,str(articleId))
        yield Request(articleUrl, callback=self.parseArtical) 
      
    def parseArtical(self, response):
        sel = Selector(response)        
        item = BlogspyderItem()     
        article_url = response.url  
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()  
        article_content=sel.xpath("//div[@id='article_content']").extract()

        item['pageTitle'] = article_name[0]
        item['pageUrl']  = article_url
        item['pageContent']  = html2text(article_content[0])
        item["pageID"] = self.pageNumber
        item["pageMD5"] =GetMD5.getMD5(item["pageUrl"])     
     
        yield item
        self.pageNumber = self.pageNumber +1
        urls = sel.xpath('//li[@class="prev_article"]/a/@href').extract()  
        if urls == []:
            nextHomePage = self.homePages.next()
            yield Request(nextHomePage, callback=self.parseHomePage)
        else:
            for url in urls:
                url = "http://blog.csdn.net" + url
                yield Request(url, callback=self.parseArtical) #no need new URL
      
    def parseHomePage(self, response):  
        jdata = json.loads(response.body)
        articleId = jdata['result'][0]['ArticleId']
        userName = jdata['result'][0]['UserName']      
        articleUrl = "http://blog.csdn.net/%s/article/details/%s" % (userName,str(articleId))
        yield Request(articleUrl, callback=self.parseArtical) 
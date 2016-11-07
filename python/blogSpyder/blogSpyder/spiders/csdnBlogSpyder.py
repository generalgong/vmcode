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
    handle_httpstatus_list = [404,444]
    def __init__(self):
        self.pageNumber =0
        self.homePages = GetUseHomePage()
        self.lastUrl = ""

  
    name = "csdnBlogSpyder"  
    #减慢爬取速度 为5s  
    download_delay = 1 
    allowed_domains = ["blog.csdn.net" , "my.csdn.net"] 
    
    start_urls = [  
        #"http://my.csdn.net/service/main/get_user_contribute?type=blog&username=datuqiqi"
        "http://blog.csdn.net/error/444.html?from=http%3a%2f%2fblog.csdn.net%2fsuiye007%2farticle%2fdetails%2f39199087"
    ]  
            
    def parse(self, response):
        if response.status > 199 and response.status < 300:          
            jdata = json.loads(response.body)
            if jdata.has_key('result') and jdata['result']!=[]:
                articleId = jdata['result'][0]['ArticleId']
                userName =  jdata['result'][0]['UserName']       
                articleUrl = "http://blog.csdn.net/%s/article/details/%s" % (userName,str(articleId))
                yield Request(articleUrl, callback=self.parseArtical) 
            else:
                nextHomePage = self.homePages.next()
                yield Request(nextHomePage, callback=self.parseHomePage)
        else:
            nextHomePage = self.homePages.next()
            yield Request(nextHomePage, callback=self.parseHomePage)
            
      
    def parseArtical(self, response):
        if response.status > 199 and response.status < 300:
            sel = Selector(response)        
            item = BlogspyderItem()     
            article_url = response.url  
            article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()  
            article_content=sel.xpath("//div[@id='article_content']").extract()
            if article_name == []:
                item['pageTitle'] = ""
            else:            
                item['pageTitle'] = article_name[0]
            item['pageUrl']  = article_url
            if article_content ==[]:
                item['pageContent']  =""
            else:
                item['pageContent']  = html2text(article_content[0])
            item["pageID"] = self.pageNumber
            #item["pageMD5"] =GetMD5.getMD5(item["pageUrl"])     
         
            yield item
            self.pageNumber = self.pageNumber +1
            urls = sel.xpath('//li[@class="prev_article"]/a/@href').extract()  
            if urls == []:
                nextHomePage = self.homePages.next()
                yield Request(nextHomePage, callback=self.parseHomePage)
            else:
                for url in urls:
                    url = "http://blog.csdn.net" + url
                    if self.lastUrl != url:
                        #yield Request(url, callback=self.parseArtical, dont_filter=True) #no need new URL
                        yield Request(url, callback=self.parseArtical, dont_filter=True)
                    else:
                        nextHomePage = self.homePages.next()
                        yield Request(nextHomePage, callback=self.parseHomePage)
                    self.lastUrl = url 
        else:
            nextHomePage = self.homePages.next()
            yield Request(nextHomePage, callback=self.parseHomePage)
      
    def parseHomePage(self, response):  
        jdata = json.loads(response.body)
        if jdata.has_key('result') and jdata['result'] != [] :
            if  jdata['result'][0].has_key('ArticleId') and jdata['result'][0].has_key('UserName'):
                articleId = jdata['result'][0]['ArticleId']
                userName = jdata['result'][0]['UserName'] 
                articleUrl = "http://blog.csdn.net/%s/article/details/%s" % (userName,str(articleId))
                yield Request(articleUrl, callback=self.parseArtical) 
            else:
                nextHomePage = self.homePages.next()
                yield Request(nextHomePage, callback=self.parseHomePage)

        else:
            nextHomePage = self.homePages.next()
            yield Request(nextHomePage, callback=self.parseHomePage)

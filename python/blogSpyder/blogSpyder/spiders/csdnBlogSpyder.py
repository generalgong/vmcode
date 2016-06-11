# -*- coding:utf-8 -*-  
#from scrapy.spiders import Spider  
from scrapy import Spider  
from scrapy.loader import ItemLoader
from scrapy.http import Request  
from scrapy.selector import Selector  
from blogSpyder.items import BlogspyderItem 
import sys
class BlogSpider(Spider):  
  
    name = "csdnBlogSpyder"  
    #减慢爬取速度 为5s  
    download_delay = 3 
    allowed_domains = ["blog.csdn.net"]  
    start_urls = [  
        #第一篇文章地址  
        "http://blog.csdn.net/u012150179/article/details/11749017"
    ]  
  
    def parse(self, response):  
        sel = Selector(response)  
  
        #items = []  
        #获得文章url和标题  
        item = BlogspyderItem()  
  
        article_url = str(response.url)  
        article_name = sel.xpath('//div[@id="article_details"]/div/h1/span/a/text()').extract()  
        article_content=sel.xpath("//div[@id='article_content']").extract()
        #print article_content
        #item['pageTitle'] = [n.encode('utf-8') for n in article_name]  
        item['pageTitle'] =  article_name  
        item['pageUrl'] = article_url.encode('utf-8')  
        item['pageContent'] =[n.encode('utf-8') for n in article_content] 
        item['pageContent'] = article_content 
        
        yield item  
  
        #获得下一篇文章的url  
        urls = sel.xpath('//li[@class="next_article"]/a/@href').extract()  
        for url in urls:
            url = "http://blog.csdn.net" + url
            print("Download URL: %s" % url)
            yield Request(url, callback=self.parse)

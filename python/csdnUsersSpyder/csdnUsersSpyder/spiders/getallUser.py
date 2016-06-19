# -*- coding:utf-8 -*- -1 
#from scrapy.spiders import Spider  
from scrapy import Spider  
from scrapy.http import Request  
from scrapy.selector import Selector  
from GetMD5 import GetMD5
from csdnUsersSpyder.items import CsdnusersspyderItem
import re
import sys
class BlogSpider(Spider):  
    def __init__(self):
        self.pageNumber =0
    name = "csdnUserScrapy"  
    #减慢爬取速度 为2s  
    download_delay = 2 
    allowed_domains = ["my.csdn.net"]  
    start_urls = [ 
    "http://my.csdn.net/sodino","http://my.csdn.net/bill_man","http://my.csdn.net/lhc2207221755","http://my.csdn.net/xgbing","http://my.csdn.net/LoongEmbedded","http://my.csdn.net/jdh99","http://my.csdn.net/zqiang_55","http://my.csdn.net/zhao_zepeng","http://my.csdn.net/linyt","http://my.csdn.net/kmyhy","http://my.csdn.net/lincyang","http://my.csdn.net/jdsjlzx","http://my.csdn.net/u011012932","http://my.csdn.net/yayun0516","http://my.csdn.net/qq_23547831","http://my.csdn.net/CHENYUFENG1991","http://my.csdn.net/qq_26787115","http://my.csdn.net/kongki","http://my.csdn.net/you23hai45","http://my.csdn.net/cometwo","http://my.csdn.net/yuanziok","http://my.csdn.net/woxueliuyun","http://my.csdn.net/gatieme","http://my.csdn.net/u010850027","http://my.csdn.net/yinwenjie","http://my.csdn.net/teamlet","http://my.csdn.net/wangyangzhizhou","http://my.csdn.net/xiaoxian8023","http://my.csdn.net/ooppookid","http://my.csdn.net/wsl211511","http://my.csdn.net/liyuanbhu","http://my.csdn.net/sxhelijian","http://my.csdn.net/raylee2007","http://my.csdn.net/luozhuang","http://my.csdn.net/shaqoneal","http://my.csdn.net/dc_726","http://my.csdn.net/tobacco5648","http://my.csdn.net/wowkk","http://my.csdn.net/csfreebird","http://my.csdn.net/xukai871105","http://my.csdn.net/tuzongxun","http://my.csdn.net/mchdba","http://my.csdn.net/lichangzai","http://my.csdn.net/leftfist","http://my.csdn.net/wonder4","http://my.csdn.net/fogyisland2000","http://my.csdn.net/smstong","http://my.csdn.net/david_520042","http://my.csdn.net/ghostbear","http://my.csdn.net/xuyaqun","http://my.csdn.net/force_eagle","http://my.csdn.net/Jmilk","http://my.csdn.net/xiangpingli","http://my.csdn.net/quqi99","http://my.csdn.net/michaelzhou224","http://my.csdn.net/zzq900503","http://my.csdn.net/pipisorry","http://my.csdn.net/zhangmike","http://my.csdn.net/foruok","http://my.csdn.net/fengbingchun","http://my.csdn.net/qingrun","http://my.csdn.net/harrymeng","http://my.csdn.net/pukuimin1226","http://my.csdn.net/lihuoming","http://my.csdn.net/zhazha1980518","http://my.csdn.net/redarmy_chen","http://my.csdn.net/yuanmeng001","http://my.csdn.net/yeka","http://my.csdn.net/xieqq","http://my.csdn.net/zhangxiaoxiang","http://my.csdn.net/oiio","http://my.csdn.net/jobchanceleo","http://my.csdn.net/broadview2006"
    ]  
    

    def parse(self, response):  
        sel = Selector(response)  
        item = CsdnusersspyderItem()
        print "response URL %s\n" % str(response.url)
        item["userName"] = str(response.url).split('/')[-1]
        relativeMarks =response.xpath("//div[@class='header clearfix']/a[@href]").extract()
        item["follow"] = []
        item["befollowed"] = []
        i = 0
        for u in relativeMarks:
            unameMark = re.findall(r'username="\b.*"',u)
            (s,e) = re.search(r'".*"',unameMark[0]).span()
            uname = unameMark[0][s+1:e-1]
            print "uname: %s\n" % uname
            if i <= 7:
                item["follow"].append(uname)
            else:
                item["befollowed"].append(uname)
            yield Request("http://my.csdn.net/"+uname , callback=self.parse)
            i += 1
        item["pageUrl"] = str(response.url)
        focusNumMark = response.xpath("//dd[@class='focus_num']").extract()[0]
        (s ,e) = re.search(r'\d+',focusNumMark).span()
        focusNum = focusNumMark[s:e].encode('utf-8')
        item["followNum"] = focusNum

        fansNumMark = response.xpath("//dd[@class='fans_num']").extract()[0]
        (s ,e) = re.search(r'\d+',fansNumMark).span()
        fansNum = fansNumMark[s:e].encode('utf-8')
        item["befollowedNum"] = fansNum
        item["pageID"] = self.pageNumber
        item["pageMD5"] =GetMD5.getMD5(item["pageUrl"])
        yield item
        self.pageNumber = self.pageNumber +1

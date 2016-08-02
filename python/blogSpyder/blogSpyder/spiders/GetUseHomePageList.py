#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb


class GetUseHomePage():
     def __init__(self):
        self.homePageList = iter(self.doSelect())
     
     def doSelect(self):
         sql = "select pageID , userName from BlogUser order by pageID ASC limit 2 "
         con = MySQLdb.connect("brian1" , "brian","general","csdn")
         cur = con.cursor()
         try:
    		  cur.execute(sql)
    		  results = cur.fetchall()
    		  fname = []
    		  for row in results:
    			fname.append(row[1])
       
    		  homePages = map(lambda x: "http://my.csdn.net/service/main/get_user_contribute?type=blog&username="+x , fname)
    	        
    		  return homePages
         except:
    	        print "execute select failed. \n" 
         finally:
             if con:
    		     con.close()
     def next(self):
        return self.homePageList.next()
       

     
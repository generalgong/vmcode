#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import division 
import MySQLdb
import time
import sys
try:
    # log = open("/home/hduser/Logs/rate.log","a")
    sql = "select count(*) from BlogUser"
    try:
        i = 1000000
        while(i>0):
             con = MySQLdb.connect("brian1" , "brian","general","csdn")
             cur = con.cursor()
             cur.execute(sql)
             (number_of_rows,)=cur.fetchone()
             logfile = open("/home/hduser/Logs/csdnUserlog.log","r")
             count = 0
             for line in enumerate(logfile):
                 count +=1
             log = open("/home/hduser/Logs/rate.log","a")
             log.write("duplicated: %d,download: %d , rate: %f \n" % (count ,number_of_rows , count/number_of_rows))
             log.close()
             logfile.close()
             con.close()
             i = i-1
             time.sleep(5* 60)


    except:
        print "connect to DB failed!\n"
finally:
        print "finally !\n" 

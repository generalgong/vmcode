# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:50:26 2016

@author: brian gong
"""

import pymysql

def con_test():
    conn = pymysql.connect(host='brian1', port=3306, user='brian', passwd='general',
    db='csdn')
    sql = "select count(*) from BlogUser"
    cur = conn.cursor()
    cur.execute(sql)
    (number_of_rows,)=cur.fetchone()
    print("*******\n"+str(number_of_rows))
        
    conn.close()
    
class CsdnUsers:
    def __init__(self):
        self.conn = pymysql.connect(host='brian1', port=3306, user='brian', passwd='general',db='csdn')
          
       
    def doSelect(self):
        self.fetchOneCursor = self.conn.cursor()
        self.fetchOneCursor.execute("SELECT pageId , userName , followNum , follows , befollowedNum , befollowed FROM BlogUser") 

    
    def __del__(self):
        print("In del function \n")
        self.conn.close()
    
    def getLines(self):
        pass

    def user2id(self , user):
        if user != "":
            sql = 'SELECT pageID from BlogUser where userName = "%s" ' % user
            cursor = self.conn.cursor()
            cursor.execute(sql)
            return cursor.fetchone()
        else:
            return ""
        
    def nextLine(self):
        return self.fetchOneCursor.fetchone()
   
class CsdnIds():
    def __init__(self):
        self.conn = pymysql.connect(host='brian1', port=3306, user='brian', passwd='general',db='csdn')
    def __del__(self):
        print("In del function \n")
        self.conn.close()      
    
    def insert(self , sql):
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            self.conn.commit()
        except:
            print("Insert error \n")
        

if __name__=="__main__":
    pass
    cuser = CsdnUsers()
    cuser.doSelect()
    csdnIds = CsdnIds()
    
    #read a Line 
    fids = []
    bfids = []
    i = 0
    while i < 838505:
        fids.clear()
        bfids.clear()
        line = cuser.nextLine()
        follows = line[3]
        if follows != "":
            fu = follows.split(',')
            for u in fu:
                print("U is :%s\n" % u)
                if cuser.user2id(u) != None:
                    (fid,) = cuser.user2id(u)
                    fids.append(fid)
                           
                     
        beFollowed  = line[5]
        if beFollowed != "":
            bfu = beFollowed.split(',')
            for u in bfu:
                if  cuser.user2id(u)!=None:
                    print("U is :%s\n" % u)
                    (bfid,) = cuser.user2id(u)
                    bfids.append(bfid)
        sql = 'insert into  BlogIDs (pageId , userName , followNum , follows , befollowedNum , befollowed) VALUES (%s , "%s" ,%s , "%s" ,%s , "%s")'\
        % (line[0] , line[1] , line[2] , ','.join(map(str,fids)) , line[4],  ','.join(map(str,bfids)))
        csdnIds.insert(sql)
        print(sql)
        i += 1
     

    #get usernames 

    #trans usernames to  ids

    #build a new line 

    #insert to ids table 
from elasticsearch import Elasticsearch
es = Elasticsearch("brian1")
itemDic = {}
itemDic["pageUrl"] = "testES"
itemDic["pageID"] = "testPageID"
itemDic["pageTitle"] = "testPageTitle"
itemDic["pageContent"] = "page count cont "

es.create(index="blog", doc_type="csdn",body=itemDic)

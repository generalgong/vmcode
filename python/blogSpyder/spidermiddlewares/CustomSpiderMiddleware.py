
class CustomSpiderMiddleware():
    def process_spider_input(self,  response , spider):
        return None
    
    def process_pider_output(self , response , result ,spider):
        return None
    def process_spider_exception(self , response, exception, spider):
        return None
    def process_start_requests(self , start_requests, spider):
        return None
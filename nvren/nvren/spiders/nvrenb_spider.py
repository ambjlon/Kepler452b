#-*-coding:utf-8 -*-
import scrapy
import re
import sys
#import scrapy.linkextractor
#import scrapy.spider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider,Rule
sys.path.append("..")
from nvren.items import NvrenItem
from nvren.mybeautifulsoup.nvrenbbs import NvrenbBs  

class NvrenbSpider(CrawlSpider):
    name = 'nvrenb'
    allowed_domains = ['www.nurenb.com']
    start_urls = ['http://www.nurenb.com']
    rules = (
    Rule(LinkExtractor(allow=[r".*/zhongyiys/\d+\.html",r".*/meironghf/\d+\.html",r".*/meirongsf/\d+\.html",r".*/meirongzs/\d+\.html",r".*/hulimb/\d+\.html",r".*/wentijifu/\d+\.html",r".*/baoshibs/\d+\.html",r".*/pihugz/\d+\.html",r".*/huazhuang/\d+\.html",r".*/fengxiong/\d+\.html",r".*/jianfei/\d+\.html",r".*/fushi/\d+\.html",r".*/meijia/\d+\.html"]),callback="myparse",follow=True),
    Rule(LinkExtractor(allow=[r".*www.nurenb.com.*"]),follow=True),
    )
    def myparse(self,response):
        nvrenb_bs = NvrenbBs()
        item = nvrenb_bs.parse_page(response)
        return item
#start_urls = ['http://www.nurenb.com/meijia/742.html']
#Rule(LinkExtractor(allow=[r".*/zhongyiys/\d+\.html",r".*/meirong/\d+\.html",r".*/huazhuang/\d+\.html",r".*/fengxiong/\d+\.html",r".*/jianfei/\d+\.html",r".*/fushi/\d+\.html",r".*/meijia/\d+\.html"]),callback="myparse",follow=True),
#Rule(LinkExtractor(allow=[r".*www.nurenb.com.*"]),follow=True),

__author__ = 'bj'
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import urllib2
import os
import string


class RegistSpider(BaseSpider):
    name = "regist"
    allowed_domains = ["regist.org"]
    start_urls = []
    start_urls.append("http://www.baidu.com")

    def parse(self, response):
        hxs =  response
        print (hxs)
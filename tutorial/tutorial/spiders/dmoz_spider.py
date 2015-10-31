# -*-coding:utf-8-*-
from scrapy.selector import HtmlXPathSelector, Selector
from tutorial.items import TutorialItem
import MySQLdb

__author__ = 'bj'
from scrapy.spider import BaseSpider


class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        # "http://www.t66y.com/thread0806.php?fid=7&search=&page=1"
        # "http://www.baidu.com"
    ]
    start_urls.append("http://www.t66y.com/thread0806.php?fid=7&search=&page=1")

    def saveInDb(self, item):
        try:
            conn = MySQLdb.connect(host='localhost', user='root', passwd='123123', db='wechat',
                                   port=3306, charset='utf8')
            cur = conn.cursor()
            execute = cur.execute("select * from t_url where url='" + item['link'] + "'")
            if execute > 0:
                return
            cur.execute(
                "insert into t_url(title,url,click_time,public_time) value('" + item[
                    'title'] + "','" +
                item['link'] + "','" + item['clickTimes'] + "','" + item['publicTime'] + "')")
            conn.commit()
        except MySQLdb.Error, e:
            print(e)
        finally:
            cur.close()
            conn.close()

    def parse(self, response):
        print("receive data")
        host = 'http://www.t66y.com/'
        hxs = Selector(response)
        sites = hxs.xpath('//tr[@class="tr3 t_one"]')
        for site in sites:
            item = TutorialItem()
            linkSite = site.xpath(
                'td[@style="text-align:left;padding-left:8px"]/h3/a[@target="_blank"]/@href')
            titleSite = site.xpath(
                'td[@style="text-align:left;padding-left:8px"]/h3/a[@target="_blank"]/text()')
            timeSite = site.xpath('td/a[@class="f10"]/text()')
            countTime = site.xpath('td[@class="tal f10 y-style"]/text()')
            if titleSite.__len__() == 0:
                continue
            for title in titleSite:
                item['title'] = title.extract()
            for link in linkSite:
                item['link'] = host + (link.extract())
            for time in timeSite:
                item['publicTime'] = (time.extract())
            for count in countTime:
                item['clickTimes'] = (count.extract())
            self.saveInDb(item)

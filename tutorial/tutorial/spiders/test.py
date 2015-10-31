#-*-coding:utf-8-*-
from scrapy.selector import Selector
import MySQLdb
import urllib
import chardet

__author__ = 'bj'


def parse(text):
    hxs = Selector(None, text, None, None, None, None)
    sites = hxs.xpath("//a[@target='_blank']")
    conn=MySQLdb.connect(host='localhost',user='root',passwd='123123',db='test',port=3306)
    cur = conn.cursor()

    for site in sites:
        titleL = site.xpath("text()").extract()
        linkL = site.xpath("@href").extract();
        for l in titleL:
            title = l;
        for l in linkL:
            link = l;
        test= u'\ufffd\ufffd\u02a6\ufffd\ufffd\u016e\ufffd\ufffd \ufffd\ufffd\u04bb\ufffd\ufffd\ufffd\ufffd\ufffd\u04b5\ufffd\u0563\ufffd\ufffd\u06b8\ufffd\ufffd\u063f\u06a3\ufffd[10P]'
        print(test.encode('utf-8'))
        print('特')
    # cur.execute("insert url_record (title,url) values('"+title.encode('utf-8')+"','"+link.encode('utf-8')+"')")
    # conn.commit()

file_io = open("demo.txt")
read = file_io.read()
# parse(read)
print (read)
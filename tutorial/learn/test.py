#-*-coding:utf-8-*-
__author__ = 'bj'
import string
import os

filecontent ='测试'
file_io = open('text.txt','wb')
file_io.write(filecontent)
file_io.flush()
file_io.close()


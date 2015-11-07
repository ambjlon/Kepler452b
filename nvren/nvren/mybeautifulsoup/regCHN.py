#-*-coding:utf-8 -*-
import sys
import re
import chardet
s = "     时间：2015-8-8 10:23:03  作者：秋风  来源：原创  查看："
print chardet.detect(s)
match = re.search(r'(.*)作者：([^ ]*)  (.*)', s)
print repr(u' ') #这是不间断空格, html中用来代替空格的一种方式,unicode编码是160, 尼玛!!!!!!
print unicode(' ','UTF-8')
if match:
    print "kk"
    print match.group()

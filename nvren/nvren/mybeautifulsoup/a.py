#-*-coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup, Comment
import sys
import re

page = urllib2.urlopen('http://www.nurenb.com/meijia/742.html')
contents = page.read()
soup = BeautifulSoup(contents,"lxml")
comments = soup.findAll(text=lambda text:isinstance(text, Comment))
[comment.extract() for comment in comments]

'''
tag = soup.findAll( "dd", class_="webBox" )
title = (tag[0].findAll( "h1" ))[0].string
tmp = unicode(( tag[0].findAll( "div", class_="addi2" ) )[0].contents[0].string).encode('UTF-8')


time = ""
match = re.search(r'\d{4}-\d{1,2}-\d{1,2} \d{2}:\d{2}', tmp)
if match:
    time =  match.group()

author = ""
match = re.search(r'(.*)作者：([^ ]*)  (.*)', tmp)
if match:
    author =  match.group(2)
source = ""
match = re.search(r'(.*)来源：([^ ]*)  (.*)', tmp)
if match:
    source = match.group(2)
viewnum = unicode(( tag[0].findAll( "div", class_="addi2" ) )[0].contents[1].string).encode('UTF-8')
commentnum = unicode(( tag[0].findAll( "div", class_="addi2" ) )[0].contents[3].string).encode('UTF-8')
'''
'''
path = ""
tag = soup.findAll("div", class_="topBody")[3].findAll("li", "a")[0]
for child in tag.children:
    if child.name == "a":
        path = path + unicode(child.string).encode('UTF-8') + ">>"
'''
'''
tags = ""
tag = soup.findAll("div", class_="mark")[0]
for child in tag.children:
    if child.name == "a":
        tags = tags + unicode(child.string).encode('UTF-8') + " "
'''

tag = soup.findAll("div", id="newsContent")[0]
text =  tag



#print title
#print time

#reload(sys)
#sys.setdefaultencoding('utf-8')

#import chardet
#print chardet.detect(unicode(tmp).encode('UTF-8'))

#paut = u"\u4f5c\u8005\uff1a"
#chn=u"([/u4e00-/u9fa5]+)"
#npspace=u"([^\u0020]*)"
#pspace = u"\u0020"
#match = re.search(r'(.*)'+paut+chn+pspace+'(.*)',tmp)
#match = re.search(r'(.*)2015(.*)',tmp)

#pattern = re.compile(r'2015')
#pattern = re.compile(r'.*(\d{4}-\d{1,2}-\d{1,2}).*')
#pattern = re.compile(r'.*\u65f6\u95f4\uff1a([^\f])* .*')
#match = pattern.match(tmp)

#-*-coding:utf-8 -*-
from bs4 import BeautifulSoup, Comment
from bs4.element import NavigableString
import sys
sys.path.append("..")
from nvren.items import NvrenItem
import re

class NvrenbBs:
    def parse_page(self, response):
        
        soup = BeautifulSoup(response.body,"lxml")
        comments = soup.findAll(text=lambda text:isinstance(text, Comment))
        [comment.extract() for comment in comments]

        tag = soup.find_all( "dd", attrs={"class":"webBox"} )

        #if len(tag)>0 and len(tag[0].findAll( "h1" )) > 0:
        #bug1
        title = (tag[0].find_all('h1'))[0].string
        tmp = unicode(( tag[0].find_all( "div", attrs={"class":"addi2" }) )[0].contents[0].string).encode('UTF-8')
        time = ''
        match = re.search(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}', tmp)
        if match:
            time =  match.group().decode('UTF-8')
        
        author = u''
        match = re.search(r'(.*)作者：([^ ]*)  (.*)', tmp)
        if match:
            author = match.group(2).decode('UTF-8')
        source = ""
        match = re.search(r'(.*)来源：([^ ]*)  (.*)', tmp)
        if match:
            source = match.group(2).decode('UTF-8')
        viewnum = (tag[0].find_all( "div", attrs={"class":"addi2"} ) )[0].contents[1].string
        commentnum = ( tag[0].find_all( "div", attrs={"class":"addi2"} ) )[0].contents[3].string

        path = ""
        tag = soup.find_all("div", attrs={"class":"topBody"})[3].find_all("li", attrs={"class":"a"})[0]
        for child in tag.children:
#            print child,type(child),isinstance(child,NavigableString)
            if not isinstance(child, NavigableString) and child.name == "a":
                path = path + unicode(child.string).encode('UTF-8') + ">>"
        path = path.decode('UTF-8')
        
        tags = ""
        tag = soup.find_all("div", attrs={"class":"mark"})[0]
        for child in tag.children:
            if not isinstance(child, NavigableString) and child.name == "a":
                tags = tags + unicode(child.string).encode('UTF-8') + " "
        tags = tags.decode('UTF-8')
        tag = soup.find_all("div", attrs={"id":"newsContent"})[0]
        #把Tag中的内容存储到一个string中, 不管有没有子节点, 或者有很多子节点
        text =  "".join(str(con) for con in tag.contents)
        text = text.decode('UTF-8')
        
        item = NvrenItem()
        item['title'] = title
        item['time'] = time
        item['author'] = author
        item['source'] = source
        item['path'] = path
        item['viewnum'] = viewnum
        item['commentnum'] = commentnum
        item['text'] = text
        item['tags'] = tags
        item['url'] = (response.url).decode("UTF-8")
        return item



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

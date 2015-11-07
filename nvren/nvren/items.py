# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NvrenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()#
    title = scrapy.Field()#文章题目
    author = scrapy.Field()#作者
    time = scrapy.Field()#发表时间
    source = scrapy.Field()#文章来源
    path = scrapy.Field()#文章在网站中的路径 e.g. 当前位置：首页 > 美甲
    viewnum = scrapy.Field()#访问数
    commentnum = scrapy.Field()#评论数
    text = scrapy.Field()#正文
    tags = scrapy.Field()#文章的属性标签
    comment = scrapy.Field()#评论
    postscript = scrapy.Field()#备注信息

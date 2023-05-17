# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YuanshenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_name = scrapy.Field()#图片名字
    img_link = scrapy.Field()#图片地址链接
    img_download_link = scrapy.Field()#图片下载链接
    img_type = scrapy.Field()#图片后缀
    img_px = scrapy.Field()#图片分辨率
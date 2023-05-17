import scrapy
from ..items import YuanshenItem


class YsSpider(scrapy.Spider):
    name = 'ys'
    allowed_domains = ['wall.alphacoders.com']
    start_urls = ['https://wall.alphacoders.com/by_sub_category.php?id=333944&name=原神+壁纸&filter=4K+Ultra+HD&lang=Chinese']
    b = 1
    base_url ='https://wall.alphacoders.com/by_sub_category.php?id=333944&name=%E5%8E%9F%E7%A5%9E+%E5%A3%81%E7%BA%B8&filter=4K+Ultra+HD&lang=Chinese&page='

    def parse(self, response):

        div = response.xpath("/html/body/div[2]/div[5]/div[1]/div")
        for i in div:

            img_id = str(i.xpath('./div/div[2]/div[2]/div[3]/span/@data-id').get()) #图片id
            # 判断id是否为空值，空值跳出本次循环
            if img_id == 'None':
                continue
            img_server = str(i.xpath('./div/div[2]/div[2]/div[3]/span/@data-server').get()) #图片的图库文件夹
            img_type = str(i.xpath('./div/div[2]/div[2]/div[3]/span/@data-type').get()) #图片后缀
            img_px = str(i.xpath('./div[1]/div[2]/div/span/text()').get()) #图片分辨率
            img_link = 'https://wall.alphacoders.com'+str(i.xpath('./div[1]/div[1]/a/@href').get())
            #拼接url https://initiate.alphacoders.com/download/wallpaper/图片id/图片数/图片类型/
            img_download_link = 'https://initiate.alphacoders.com/download/wallpaper/'+ img_id +'/'+img_server+'/'+ img_type+'/'
            # print(img_px)
            # print(img_id)
            # print(img_server)
            # print(img_type)
            # print(img_link)
            # print(img_download_link)
            bookitem = YuanshenItem(img_download_link=img_download_link,img_name=img_id,img_type=img_type
                                    ,img_px=img_px,img_link=img_link)
            yield bookitem

        if self.b < 64:
            self.b = self.b + 1
            url = self.base_url + str(self.b)
            print('正在爬取：', url)
            yield scrapy.Request(url=url, callback=self.parse)
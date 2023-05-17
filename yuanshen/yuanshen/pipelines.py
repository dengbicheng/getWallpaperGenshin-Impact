from scrapy.pipelines.files import FilesPipeline
import scrapy
import pymysql
class DownloadPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        url = item.get('img_download_link')	#图片地址链接
        name = item.get('img_name')	#图片名字
        name_type = item.get('img_type')
        img_px = item.get('img_px')
        # 依次对图片地址发送请求，meta用于传递视图片的文件名
        yield scrapy.Request(url=url, meta={'name':name+'-'+img_px+'.'+name_type})
    def file_path(self, request, response=None, info=None, *, item=None):
        filename = request.meta['name']  # 获取图片文件名
        return filename  # 返回下载的图片文件名

    def item_completed(self, results, item, info):
        return item


class MysqlPipeline():
    #连接数据库
    def open_spider(self,spider):
        print('=======open_spider=======')
        # 获取settings属性
        host = spider.settings.get('DB_HOST')  # 主机
        port = spider.settings.get('DB_PORT')  # 端口号
        user = spider.settings.get('DB_USER')  # 用户名
        password = spider.settings.get('DB_PASSWORD')  # 密码
        db = spider.settings.get('DB_NAME')  # 数据库名
        charset = spider.settings.get('DB_CHARSET')  # 字符编码
        # 连接数据库pymysql.connect(host,port,user,password,db,charset)
        self.connect = pymysql.connect(host=host, port=port, user=user, password=password, db=db, 			 charset=charset)
        self.cursor = self.connect.cursor()

    #数据库写入数据
    def process_item(self,item,spider):
        # print('=======process_item=======')
        img_id = item.get('img_name')
        img_link = item.get('img_link')
        img_download_link = item.get('img_download_link')
        img_px = item.get('img_px')
        img_type = item.get('img_type')
        sql = 'insert into img_yuanshen(img_id,img_link,img_download_link,img_px,img_type) values ("{}","{}","{}","{}","{}")'\
            .format(str(img_id),str(img_link),str(img_download_link),str(img_px),str(img_type))

        # 执行sql语句
        self.cursor.execute(sql)
        # 提交
        self.connect.commit()
        return item
    #关掉连接
    def close_spider(self,spider):
        print('=======close_spider=======')
        # 关闭数据库连接
        self.cursor.close()
        self.connect.close()
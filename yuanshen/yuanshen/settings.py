
BOT_NAME = 'yuanshen'

SPIDER_MODULES = ['yuanshen.spiders']
NEWSPIDER_MODULE = 'yuanshen.spiders'

ITEM_PIPELINES = {
#    'yuanshen.pipelines.YuanshenPipeline': 301,
     'yuanshen.pipelines.DownloadPipeline' : 299,
     'yuanshen.pipelines.MysqlPipeline': 300
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

#、是否遵守robots.txt规则,默认TRUE
ROBOTSTXT_OBEY = False
#用户代理
USER_AGENT_LIST=[
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56'
]
DEFAULT_REQUEST_HEADERS = {
    'accept': 'image/webp,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    'referer': 'https://www.taobao.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36',
}
# 随机请求头
import random
USER_AGENT = random.choice(USER_AGENT_LIST)

# 保存文件路径
FILES_STORE = r'C:\Users\19456\Pictures\素材\原神动漫图片'
# 设置并发数
CONCURRENT_REQUESTS = 3
# 设置下载延时
DOWNLOAD_DELAY = 3
#关闭cookie
COOKIES_ENABLED = False
MEDIA_ALLOW_REDIRECTS = True
# 启用后，当从相同的网站获取数据时，Scrapy将会等待一个随机的值，延迟时间为0.5到1.5之间的一个随机值乘以DOWNLOAD_DELAY
RANDOMIZE_DOWNLOAD_DELAY = True

#日志
LOG_LEVEL = 'WARNING'  # 设置日志级别
from datetime import datetime
import os
today = datetime.now()
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)
LOG_FILE = "{}/scrapy_{}_{}_{}.log".format(LOG_DIR, today.year, today.month, today.day)

#设置mysql数据库基础参数
DB_HOST = 'localhost' #主机名  本地主机
DB_PORT = 3306  #端口号默认是3306
DB_USER = 'root' #用户名
DB_PASSWORD = '123456789'#密码
DB_NAME = 'Reptile' #数据库名
DB_CHARSET = 'utf8'#编码

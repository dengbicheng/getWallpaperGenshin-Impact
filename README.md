# 原神壁纸爬虫

这是一个使用Scrapy框架编写的原神壁纸爬虫。该爬虫可以从"[https://wall.alphacoders.com"网站爬取原神壁纸的相关信息，并将其保存到本地或进行其他进一步处理。](https://wall.alphacoders.xn--com"%2C-cu3k85de4dhb038agbb30zvxiy0aq55brhhulbp71akwdb6siqlnmkfp8ac3xp85bmillgs0jdkv1aiql386a2meln2htpycda./)

## 简介

本爬虫使用Python编写，基于Scrapy框架进行开发。它能够自动访问指定网页，提取壁纸的id、图库文件夹、后缀、分辨率等信息，并将其封装到`YuanshenItem`对象中。通过使用Scrapy的异步处理和自动请求功能，可以高效地爬取多页数据。

## 功能特性

- 爬取原神壁纸的id、图库文件夹、后缀、分辨率等信息
- 支持自动翻页，可以爬取多页壁纸数据
- 保存爬取到的壁纸信息到本地或其他媒介
- 可以根据需要进一步处理爬取到的数据，如保存到数据库或进行数据分析等

## 安装依赖

在运行本爬虫之前，确保已经安装以下依赖项：

- Python 3.x
- Scrapy

可以使用以下命令安装Scrapy：

```
pip install scrapy
```

## 使用方法

1. 使用git克隆本项目到本地：

2. 运行爬虫：

   ```
   scrapy crawl ys
   ```

   或者点击`启动.py`运行

3. 等待爬虫完成数据爬取。爬取到的壁纸信息将保存在指定的位置。

## 配置选项

可以在`YsSpider`类中的属性部分进行一些配置选项的修改，以满足特定需求。例如：

- `name`：设置爬虫的名称
- `allowed_domains`：设置允许爬取的域名
- `start_urls`：设置起始URL
- 其他自定义属性和方法

请根据实际需求进行配置。

### settings.py

- `BOT_NAME`：设置爬虫的名称为'yuanshen'。
- `SPIDER_MODULES`和`NEWSPIDER_MODULE`：指定爬虫模块的位置。
- `ITEM_PIPELINES`：设置数据处理的管道。在这个配置中，有两个管道被启用：`DownloadPipeline`和`MysqlPipeline`，并且它们分别被赋予了优先级299和300。注释掉的`YuanshenPipeline`则没有被启用。
- `REQUEST_FINGERPRINTER_IMPLEMENTATION`：设置请求指纹实现的版本为'2.7'。
- `TWISTED_REACTOR`：设置Twisted的反应器为'AsyncioSelectorReactor'，以支持异步的IO操作。
- `ROBOTSTXT_OBEY`：设置是否遵守robots.txt规则为False，即不遵守。
- `USER_AGENT_LIST`和`USER_AGENT`：设置用户代理的列表和随机选择的用户代理。用户代理是用于模拟浏览器请求的标识。
- `DEFAULT_REQUEST_HEADERS`：设置默认的请求头，包括接受的内容类型、语言、Referer和用户代理等。
- `FILES_STORE`：设置保存文件的路径，即壁纸文件的存储位置。
- `CONCURRENT_REQUESTS`：设置并发请求数，即同时发送的请求数量。
- `DOWNLOAD_DELAY`：设置下载延迟，即每个请求之间的间隔时间。
- `COOKIES_ENABLED`：设置是否启用cookie，这里设置为False，即禁用cookie。
- `MEDIA_ALLOW_REDIRECTS`：设置是否允许重定向。
- `RANDOMIZE_DOWNLOAD_DELAY`：设置是否随机化下载延迟。
- `LOG_LEVEL`、`LOG_DIR`和`LOG_FILE`：设置日志级别和日志文件的保存路径。

此外，还有一些其他的配置参数，如数据库的连接参数(DB_HOST、DB_PORT、DB_USER、DB_PASSWORD、DB_NAME和DB_CHARSET)用于设置MySQL数据库的基本信息。

这些配置项可以根据实际需求进行修改和调整，以适应不同的爬取场景和需求。

### pipelines.py

`DownloadPipeline`继承自Scrapy内置的`FilesPipeline`，用于下载文件。它重写了`get_media_requests`方法，通过yield返回请求对象，其中包含了图片的下载链接和文件名。`file_path`方法用于定义文件的保存路径，这里直接返回文件名。`item_completed`方法返回item对象，表示处理完毕。

`MysqlPipeline`用于将数据存储到MySQL数据库中。在`open_spider`方法中建立数据库连接，获取配置信息并初始化数据库连接。`process_item`方法用于处理item对象，提取图片信息，并执行插入数据库的操作。最后，在`close_spider`方法中关闭数据库连接。

这两个管道可以根据需求进行自定义和修改，以适应具体的爬取任务和数据存储需求。

## 数据处理

爬取到的壁纸信息将封装到`YuanshenItem`对象中，并通过Scrapy的处理管道进行进一步处理。你可以根据需要自定义处理管道，例如保存到数据库、存储到文件、进行数据分析等。

## 注意事项

- 爬取网站的数据是有限制的，请遵守网站的使用规则，不要过于频繁地请求数据，以免造成不必要的麻烦。
- 请在合法的情况下使用本爬虫，遵守相关法律法规。
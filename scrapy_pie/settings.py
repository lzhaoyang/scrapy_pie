# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_pie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import datetime

BOT_NAME = 'scrapy_pie'

SPIDER_MODULES = ['scrapy_pie.spiders']
NEWSPIDER_MODULE = 'scrapy_pie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapy_pie.middlewares.ScrapyPieSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'scrapy_pie.middlewares.ScrapyPieDownloaderMiddleware': 543,
    # ss代理
    'scrapy_pie.middlewares.ScrapyPieProxyDownMiddleware': 1,

}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'scrapy_pie.pipelines.ScrapyPiePipeline': 300,

    # javbus(在javbus中单独指定)
    # 'scrapy_pie.pipelines.ScrapiesPipelineSync': 5,

    # shtorrent
    # 'scrapy_pie.pipelines.ShtorrentDataSyncStorePipeline': 6,
    # shtorrent file
    # sht图片
    # 'scrapy_pie.pipelines.ShtorrentImageDownloadPipeline': 1,
    # sht torrent
    # 'scrapy_pie.pipelines.ShtorrentTorrentDownloadPipeline': 3,

    # 启用scrapy自带的图片下载ImagesPipeline
    'scrapy.pipelines.images.ImagesPipeline': None,

    # 启用scrapy自带的文件下载FilesPipeline
    'scrapy.pipelines.files.FilesPipeline': None,

    # 如果采用自定义的CustomImagesPipeline，需要将自带的ImagesPipeline设置为None。
    # 'NovelSpider.pipelines.CustomImagesPipeline': 1,
    # 'NovelSpider.pipelines.MongoPipeline': 2
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# 数据库连接
# MYSQL_HOST = '127.0.0.1'
# MYSQL_DBNAME = 'javbus_db'
# MYSQL_USER = 'root'
# MYSQL_PASS = '123456'

# vm数据库(这里不集中定义，分散在spider的custom_setting中)
# 数据库共用
MYSQL_HOST = '192.168.11.117'
MYSQL_DBNAME = {"scrapy_pie": "scrapy_pie_db"}
MYSQL_USER = 'root'
MYSQL_PASS = 'sunriseme1994'
# # 配置图片的保存目录
# IMAGES_STORE = './resourcedata/sht'
# # 在ImagesPipeline进行下载图片是，配置图片对应的Item字段
# # 图片下载链接字段
# IMAGES_URLS_FIELD = 'film_preview_url'
# # 文件的保存目录 ./resourcedata/sht
# FILES_STORE = './resourcedata/sht'
# # 文件下载路径字段
# FILES_URLS_FIELD = 'torrent_url'

# 开启日志
# LOG_LEVEL = 'DEBUG'
# to_day = datetime.datetime.now()
# log_file_path = 'log/scrapy_{}_{}_{}.log'.format(to_day.year, to_day.month, to_day.day)
# LOG_FILE = log_file_path

BOT_NAME = 'youtubescraper'
SPIDER_MODULES = ['yt.spiders.channel']
NEWSPIDER_MODULE = 'yt.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 28  # 28

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

#REDIRECT_ENABLED = False
#HTTPPROXY_ENABLED = False
#RETRY_ENABLED = False
#HTTPAUTH_ENABLED = False
#REDIRECT_MAX_TIMES = 2

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = True

# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'yt.middlewares.YtSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'yt.middlewares.YtDownloaderMiddleware': 543,
# }

# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'yt.pipelines.DatabasePipeline': 300
}

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = False
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Scrapy settings for exam project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "exam"

SPIDER_MODULES = ["exam.spiders"]
NEWSPIDER_MODULE = "exam.spiders"


# Crawl responsibly by identifying yourself on the user-agent

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:

# Disable cookies (enabled by default)

# Disable Telnet Console (enabled by default)

# Override the default request headers:
#    "Accept-Language": "en",

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#    "exam.middlewares.ExamSpiderMiddleware": 543,

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#    "exam.middlewares.ExamDownloaderMiddleware": 543,

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#    "scrapy.extensions.telnet.TelnetConsole": None,

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#    "exam.pipelines.ExamPipeline": 300,

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# The initial download delay
# The maximum download delay to be set in case of high latencies
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Enable showing throttling stats for every response received:

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

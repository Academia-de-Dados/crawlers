BOT_NAME = "exam"

SPIDER_MODULES = ["exam.spiders"]
NEWSPIDER_MODULE = "exam.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

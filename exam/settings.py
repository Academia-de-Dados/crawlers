BOT_NAME = "exam"

SPIDER_MODULES = ["exam.spiders"]
NEWSPIDER_MODULE = "exam.spiders"

ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    "exam.pipelines.ExamPipeline": 300,
}

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

MONGO_URI = "mongodb://root:root@localhost:27017/"

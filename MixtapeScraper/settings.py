 # Scrapy settings for MixtapeScraper project

SPIDER_MODULES = ['MixtapeScraper.spiders']
NEWSPIDER_MODULE = 'MixtapeScraper.spiders'
DEFAULT_ITEM_CLASS = 'MixtapeScraper.items.Website'

ITEM_PIPELINES = {'MixtapeScraper.pipelines.CSVPipeline': 300 }


 # Scrapy settings for MixtapeScraper project

SPIDER_MODULES = ['MixtapeScraper.spiders']
NEWSPIDER_MODULE = 'MixtapeScraper.spiders'
DEFAULT_ITEM_CLASS = 'MixtapeScraper.items.Website'

ITEM_PIPELINES = {'MixtapeScraper.pipelines.CSVPipeline': 300 }

'''FEED_EXPORTERS = {
    'csv': 'MixtapeScraper.csv_item_exporter.MixtapeScraperCsvItemExporter',
}

FIELDS_TO_EXPORT = [
    'name',
    'url',
    'views',
    'streams'
]'''
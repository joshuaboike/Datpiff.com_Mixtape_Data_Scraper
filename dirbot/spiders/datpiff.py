from scrapy.spider import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["datpiff.com"]
    start_urls = [
        "http://www.datpiff.com/CB-Smooth-CB-Smooth-Country-Boy-Smooth-mixtape.655710.html",
        "http://www.datpiff.com/Wale-x-A-Trak-Festivus-mixtape.675330.html",
    ]

    '''def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items'''

    def parse(self, response):
        filename = response.url.split("/")[-2]
        filename = filename[-1].split("-")[1]
        with open(filename, 'wb') as f:
            f.write(response.body)
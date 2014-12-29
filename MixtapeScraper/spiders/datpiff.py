from scrapy.spider import Spider
from scrapy.selector import Selector

from MixtapeScraper.items import Website

import datetime


class DatpiffSpider(Spider):
    name = "datpiff"
    allowed_domains = ["datpiff.com"]
    start_urls = [
        "http://www.datpiff.com/CB-Smooth-CB-Smooth-Country-Boy-Smooth-mixtape.655710.html",
        "http://www.datpiff.com/Wale-x-A-Trak-Festivus-mixtape.675330.html",
        "http://www.datpiff.com/Mick-Jenkins-Trees-And-Truths-mixtape.481765.html",
        "http://www.datpiff.com/Mick-Jenkins-The-Waters-mixtape.638443.html",
        "http://www.datpiff.com/Vic-Mensa-Innanetape-mixtape.536504.html",
        "http://www.datpiff.com/Earl-Sweatshirt-Earl-mixtape.179914.html",
        "http://www.datpiff.com/Tyler-The-Creator-Bastard-mixtape.184449.html",
        "http://www.datpiff.com/Lucki-Eck-Body-High-mixtape.637425.html",
        "http://www.datpiff.com/Chance-The-Rapper-10-Day-mixtape.337986.html",
        "http://www.datpiff.com/Joey-Bada-1999-mixtape.361792.html",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.datpiff.com/Wale-x-A-Trak-Festivus-mixtape.675330.html
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//div[@id="leftColumnWide"]')
        items = []

        for site in sites:
            item = Website()

            item['name'] = site.xpath('div[@class="module1"]/div[@class="content"]/h1/span[@itemprop="byArtist"]/text()').extract()
    
            item['url'] = site.xpath('div[@class="module1"]/a/@href').extract()

            item['views'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="description"]/div[@class="stats mixtape"]/div[@class="number views"]/text()').extract()

            item['streams'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="description"]/div[@class="stats mixtape"]/div[@class="number streams"]/text()').extract()

            item['downloads'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="description"]/div[@class="stats mixtape"]/div[@class="number downloads"]/text()').extract()

            '''item['ratingValue'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="description"]/div[@itemprop="aggregateRating"]/meta[@itemprop="ratingValue"]').extract()
            print
            print
            print 'RATINGVALUE:', item['ratingValue']

            items.append(item)'''

            #DJ dummy variable
            item['DJ'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="detailbar"]/div[@class="left"]/div/span[@class="charcoal"]/text()').extract()
            if item['DJ'] == [u'N/A']:
                item['DJ'] = 0
            else:
                item['DJ']= 1

            item['monthdayReleased'] = site.xpath('div[@class="module1"]/div[@class="content"]/div[@class="detailbar"]/div[@class="right"]/div/span[@class="charcoal"]/text()').extract()
            date = str(item['monthdayReleased'])[3:-2]
            year = date.split("/")[2]
            month = date.split("/")[1]
            day = date.split("/")[0]
            item['monthdayReleased'] = month

            #Weekday dummy variables
            releaseDate = datetime.date(int(year),int(day), int(month))
            weekday = releaseDate.strftime("%A")
            item['mondayDummy'] = 0
            item['tuesdayDummy'] = 0
            item['wednesdayDummy'] = 0
            item['thursdayDummy'] = 0
            item['fridayDummy'] = 0
            item['saturdayDummy'] = 0
            if weekday == 'Monday':
                item['mondayDummy'] = 1
            elif weekday == 'Tuesday':
                item['tuesdayDummy'] = 1
            elif weekday == 'Weekday':
                item['wednesdayDummy'] = 1
            elif weekday == 'Thursday':
                item['thursdayDummy'] = 1
            elif weekday == 'Friday':
                item['fridayDummy'] = 1
            elif weekday == 'Saturday':
                item['saturdayDummy'] = 1



            '''print
            print
            print 'DATESINCERELEASED:', item['dateSinceReleased']'''

        return item

    '''def parse(self, response):
        filename = response.url.split("/")[-1]
        filename = filename.split("-")[0]
        with open(filename, 'wb') as f:
            f.write(response.body)'''
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from MixtapeScraper.items import Website

import datetime
import scrapy


class DatpiffSpider(Spider):
    name = "datpiff"
    allowed_domains = ["datpiff.com"]
    start_urls = ["http://www.datpiff.com/mixtapes/celebrated"]
    '''start_urls = [
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
    ]'''

    def parse(self, response):
        '''this function takes the initial datpiff.com webpage that contains all the subsequent mixtape links, scrapes the 
        links, and puts them into list secondary_urls. These urls are passed to XXXXXX for further scraping off of their
        own individual pages'''

        sel = Selector(response)
        sites = sel.xpath('//div[@id="leftColumnWide"]')
        secondary_urls = []

        for site in sites:
            base_url = "http://datpiff.com"
            tempName = site.xpath('//div[@class="contentItemInner"]/a[1]/@href').extract()
        
        for temp in tempName:
            secondary_urls.append(base_url + temp)

        # Setting up a new request to pass to the get_DT method, also passing along the 'item' class meta data
        '''request = scrapy.Request(website, callback=self.mixtapePage)
        request.meta['item'] = item
        yield request'''

        requestList = []
        for url in secondary_urls:
            request = Request(url, callback=self.mixtapePage)
            requestList.append(request)
        
        return requestList

    def mixtapePage(self, response):

        sel = Selector(response)
        sites = sel.xpath('//div[@id="leftColumnWide"]')
        items = []

        for site in sites:

            item = Website()

            item['artistName'] = site.xpath('//h1/span[@itemprop="byArtist"]/text()').extract()

            item['mixtapeName'] = site.xpath('//h1/span[@class="timesGray"]/text()').extract()
    
            item['url'] = site.xpath('meta[@itemprop="url"]/@content').extract()

            item['views'] = site.xpath('//div[@class="number views"][1]/text()').extract()

            item['streams'] = site.xpath('//div[@class="stats mixtape"]/div[@class="number streams"]/text()').extract()

            item['downloads'] = site.xpath('//div[@class="number downloads"]/text()').extract()

            #item['ratingValue'] = site.xpath('//meta[@itemprop = "ratingValue"]/@content').extract() 

            #item['ratingCount'] = site.xpath('//meta[@itemprop = "ratingCount"]/@content').extract() 

            #item['bestRating'] = site.xpath('//meta[@itemprop = "bestRating"]/@content').extract() 

            #item['worstRating'] = site.xpath('//meta[@itemprop = "worstRating"]/@content').extract() #Didn't end up using these

            item['numberTracks'] = site.xpath('meta[@itemprop="numTracks"]/@content').extract()

            #Duration calculations
            totalDurationSec = 0
            item['trackDuration'] = site.xpath('//ul[@class="tracklist"]/li[@itemprop="track"]/meta[@itemprop="duration"]/@content').extract()
            for track in item['trackDuration']:
                tempTrack = track[2:-1].split("M")
                trackSeconds = (int(tempTrack[0]) * 60) + int(tempTrack[1])
                totalDurationSec += trackSeconds
            item['projectDuration'] = totalDurationSec / 60.0

            #numberFeatures and percentFeatures calculations
            numTracks = float(str(item['numberTracks'])[3:-2])
            songsWithFeatures = 0
            featureChecks = (' ft ', '(ft', '[ft', ' ft.', ' feat ', '(feat', '[feat', ' feat.', 'featuring')
            item['trackTitle'] = site.xpath('//ul[@class="tracklist"]/li[@itemprop="track"]/span[@class="trackTitle"]/text()').extract()
            for track in item['trackTitle']:
                trackLower = track.lower()
                #first checks to see if the track has any features at all
                if any(i in trackLower for i in featureChecks):
                    songsWithFeatures += 1
                else:
                    continue
            item['percentFeatures'] = songsWithFeatures / numTracks

            #DJ dummy variable
            item['djDummy'] = site.xpath('//div[@class="detailbar"]/div[@class="left"]/div/span[@class="charcoal"]/text()').extract()
            if item['djDummy'] == [u'N/A']:
                item['djDummy'] = 0
            else:
                item['djDummy'] = 1

            #Sponsored dummy variable
            item['sponsoredDummy'] = site.xpath('//div[@class="awardBanner sponsor"]/span/text()').extract()
            if item['sponsoredDummy'] == [u'SPONSORED:']:
                item['sponsoredDummy'] = 1
            else:
                item['sponsoredDummy'] = 0
         
            #Official dummmy variable
            item['officialDummy'] = site.xpath('//div[@class="awardBanner official"]').extract()
            if item['officialDummy']:
                item['officialDummy'] = 1
            else:
                item['officialDummy'] = 0

            #Date variables
            item['monthdayReleased'] = site.xpath('//div[@class="detailbar"]/div[@class="right"]/div/span[@class="charcoal"]/text()').extract()
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

            #items.append(item)

        return item

    '''def parse(self, response):
        filename = response.url.split("/")[-1]
        filename = filename.split("-")[0]
        with open(filename, 'wb') as f:
            f.write(response.body)'''
from scrapy.item import Item, Field


class Website(Item):

    name = Field()
    url = Field()
    views = Field()
    streams = Field()
    downloads = Field()
    ratingValue = Field()
    ratingCount = Field()
    bestRating = Field()
    worstRating = Field()
    DJ = Field()
    monthdayReleased = Field()
    mondayDummy = Field()
    tuesdayDummy = Field()
    wednesdayDummy = Field()
    thursdayDummy = Field()
    fridayDummy = Field()
    saturdayDummy = Field()
    monthReleased = Field()
    dateSinceReleased = Field()
    sponsored = Field()
    numberTracks = Field()
    numberFeatures = Field()
    numberProducers = Field()
    percentFeatures = Field()
    percentProducers = Field()


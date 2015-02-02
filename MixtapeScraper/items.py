from scrapy.item import Item, Field


class Website(Item):

    artistName = Field()
    mixtapeName = Field()
    url = Field()
    views = Field()
    streams = Field()
    downloads = Field()
    numberTracks = Field()
    trackDuration = Field()
    projectDuration = Field()
    trackTitle = Field()
    percentFeatures = Field()
    productionDummy = Field()
    daysSinceRelease = Field()
    djDummy = Field()

    #complete or in progress but not useful
    monthdayReleased = Field()
    monthReleased = Field()
    numberFeatures = Field()
    sponsoredDummy = Field()
    officialDummy = Field()
    mondayDummy = Field()
    tuesdayDummy = Field()
    wednesdayDummy = Field()
    thursdayDummy = Field()
    fridayDummy = Field()
    saturdayDummy = Field()
    ratingValue = Field()
    ratingCount = Field()
    bestRating = Field()
    worstRating = Field()

    



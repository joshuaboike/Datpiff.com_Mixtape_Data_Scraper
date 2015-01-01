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
    numberFeatures = Field()
    percentFeatures = Field()
    '''ratingValue = Field()
    ratingCount = Field()
    bestRating = Field()
    worstRating = Field()''' #Didn't use these
    djDummy = Field()
    sponsoredDummy = Field()
    officialDummy = Field()
    monthdayReleased = Field()
    mondayDummy = Field()
    tuesdayDummy = Field()
    wednesdayDummy = Field()
    thursdayDummy = Field()
    fridayDummy = Field()
    saturdayDummy = Field()
    monthReleased = Field()
    dateSinceReleased = Field()
    numberProducers = Field()
    percentProducers = Field()


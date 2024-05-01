from scrapy import Item, Field
import scrapy

class CryptoCurrency(Item):
    id = scrapy.Field()
    symbol = scrapy.Field()
    datetime = scrapy.Field()
    # datetime_close = scrapy.Field()
    open = scrapy.Field()
    high = scrapy.Field()
    low = scrapy.Field()
    close = scrapy.Field()
    volume = scrapy.Field()
    # marketCap = scrapy.Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Kennesaw_spiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pageid = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field()
    emails = scrapy.Field()


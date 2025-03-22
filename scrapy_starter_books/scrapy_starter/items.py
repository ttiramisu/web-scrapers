# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyStarterItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()

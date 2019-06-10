# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Stations(scrapy.Item):
    name = scrapy.Field()
    stations = scrapy.Field()
    created_at = scrapy.Field()
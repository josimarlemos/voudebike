# -*- coding: utf-8 -*-
import os
import redis
import scrapy


class BikesampaSpider(scrapy.Spider):
    name = 'bikesampa'
    allowed_domains = ['bikeitau.com.br']
    start_urls = ['http://bikeitau.com.br/bikesampa/']

    def __init__(self):
        self.redis = redis.Redis.from_url(os.environ.get('REDIS_URL'))

    def parse(self, response):
        lat = self.fetch(response, 'lat_arr')
        lng = self.fetch(response, 'long_arr')

        for station in self.merge(lat, lng):
            yield station

    def fetch(self, response, field):
        query = "//input[@id='{}']/@value".format(field)

        result = response.xpath(query).get()

        return [item.strip() for item in result.split(';')]

    def merge(self, lat, lng):
        return [{'lat': lat, 'lng': lng} for lat, lng in zip(lat, lng)]

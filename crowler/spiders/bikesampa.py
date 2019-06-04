# -*- coding: utf-8 -*-
import scrapy
import datetime
from crowler.items import Service


class BikesampaSpider(scrapy.Spider):
    name = 'bikesampa'
    allowed_domains = ['bikeitau.com.br']
    start_urls = ['http://bikeitau.com.br/bikesampa/']

    def parse(self, response):
        lat = self.fetch(response, 'lat_arr')
        lng = self.fetch(response, 'long_arr')

        yield Service(
            name=self.name,
            stations=self.merge(lat, lng),
            created_at=datetime.datetime.now()
        )


    def fetch(self, response, field):
        query = "//input[@id='{}']/@value".format(field)

        result = response.xpath(query).get()
        
        return [item.strip() for item in result.split(';')]

    def merge(self, lat, lng):
        return [{'lat': lat, 'lng': lng} for lat, lng in zip(lat, lng)]
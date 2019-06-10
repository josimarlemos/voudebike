# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import json
import redis


class RedisPipeline(object):
    def __init__(self):
        url = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')
        self.redis = redis.Redis.from_url(url)

    def process_item(self, item, spider):
        created_at = item['created_at']
        key = "services:{}".format(created_at)
        
        self.redis.setex(key, 60*60, json.dumps(dict(item)))

        return item
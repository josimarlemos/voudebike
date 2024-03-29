import os
import json
import redis
import subprocess
from flask import Flask


app = Flask(__name__)

url = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379')
redis = redis.Redis.from_url(url)

@app.route('/api/stations')
def stations():
    try:
        keys = [
            key.decode().split(':').pop()
            for key in redis.keys('services:*')
        ]

        keys.sort()

        key = 'services:{}'.format(keys.pop())

        return redis.get(key)
    except:
        subprocess.Popen(['scrapy', 'crawl', 'bikesampa'])

        return json.dumps([])
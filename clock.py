import subprocess
from apscheduler.schedulers.blocking import BlockingScheduler


scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=30)
def scrapy_crawl():
    subprocess.run(['scrapy', 'crawl', 'bikesampa'])


scheduler.start()

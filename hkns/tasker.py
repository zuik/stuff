import requests, time
from celery import Celery

from pymongo import MongoClient

client = MongoClient()
db = client['hkns']

HEADERS = {
    "User-Agent": "Meow!"
}

ITEM_ROOT = "https://hacker-news.firebaseio.com/v0/item/"
TOP_ROOT = "https://hacker-news.firebaseio.com/v0/topstories.json"
NEW_ROOT = "https://hacker-news.firebaseio.com/v0/newstories.json"
BEST_ROOT = "https://hacker-news.firebaseio.com/v0/beststories.json"
MAX_ROOT = "https://hacker-news.firebaseio.com/v0/maxitem.json"

app = Celery()

app.config_from_object('celeryconfig')


@app.on_after_configure.connect
def setup(sender, **kwargs):
    sender.add_periodic_task(600.0, get_tops.s())
    sender.add_periodic_task(600.0, get_news.s())
    sender.add_periodic_task(600.0, get_bests.s())
    sender.add_periodic_task(600.0, max_id.s())


@app.task(name='tops')
def get_tops():
    r = requests.get(TOP_ROOT, headers=HEADERS)
    if r.status_code == 200:
        tops = r.json()
        db['raw_time'].insert_one({
            "bests": tops,
            "time": time.time(),
            "type": "top",
        })
        return tops


@app.task(name='news')
def get_news():
    r = requests.get(NEW_ROOT, headers=HEADERS)
    if r.status_code == 200:
        news = r.json()
        db['raw_time'].insert_one({
            "bests": news,
            "time": time.time(),
            "type": "new",
        })
        return news


@app.task(name='bests')
def get_bests():
    r = requests.get(BEST_ROOT, headers=HEADERS)
    if r.status_code == 200:
        bests = r.json()
        db['raw_time'].insert_one({
            "bests": bests,
            "time": time.time(),
            "type": "best",
        })
        return bests


@app.task(name='max_id')
def max_id():
    r = requests.get(MAX_ROOT, headers=HEADERS)
    if r.status_code == 200:
        mid = int(r.text)
        db['raw_time'].insert_one({
            "id": mid,
            "time": time.time(),
            "type": "max_id",
        })
        return mid

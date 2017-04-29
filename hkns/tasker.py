import json

import pymongo
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
    sender.add_periodic_task(30.0, get_tops.s())
    sender.add_periodic_task(30.0, get_news.s())
    sender.add_periodic_task(30.0, get_bests.s())
    sender.add_periodic_task(30.0, max_id.s())
    sender.add_periodic_task(15.0, scrape_story.s())


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


@app.task(name='stories')
def get_story(id):
    url = "{}{}.json".format(ITEM_ROOT, id)
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        data = r.json()
        data['_id'] = id
        dd = db['items'].find_one({"_id": id})
        if dd:
            print("Duplicate")
            return "Duplicate"
        else:
            db['items'].insert_one(data)
            print("Insert {}".format(id))
    return


@app.task(name="scrape_stories")
def scrape_story():
    d = db['raw_time'].find_one({"type": "max_id"}, sort=[("time", -1)])
    if d:
        lid = d['id']
        mid = db['items'].find_one(sort=[("time", -1)])
        if mid:
            while int(lid) > int(mid['id']):
                print(lid, mid['id'])
                get_story.delay(lid)
                lid -= 1
        else:
            get_story.delay(lid)
    return

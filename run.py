from hkns.scraper import HKitem, max_id, get_bests, get_news, get_tops, log
from hkns.config import db
from celery import Celery

app = Celery()

app.config_from_object('hkns.config')


@app.on_after_configure.connect
def setup(sender, **kwargs):
    sender.add_periodic_task(301.0, get_ranking.s())
    sender.add_periodic_task(151.0, scrape_story.s())


@app.task(name="ranking")
def get_ranking():
    bests = get_bests()
    if bests:
        return "Got bests"
    else:
        log("error", {"bests": "no bests"})
        return "Error best"
    tops = get_tops()
    if tops:
        return "Got tops"
    else:
        log("error", {"tops": "no tops"})
        return "Error top"


@app.task(name="item")
def get_item(_id):
    item = HKitem(_id)
    item.get_data()
    if item.data:
        return "Got {}".format(_id)


@app.task(name='scrape_story')
def scrape_story():
    """
    Every once in a while, we scrape the max_id, 
    we would get all of the item from that max_id to our current latest item.
    :return: None
    """
    d = max_id()
    if d:
        lid = d
        mid = db['items'].find_one(sort=[("id", -1)])
        if mid:
            while int(lid) > int(mid['id']):
                get_item.delay(lid)
                lid -= 1
        else:
            get_item.delay(lid)
    return


if __name__ == "__main__":
    _max = max_id()
    print(_max)
    # a = HKitem(_max)
    # a.get_data()
    # print(a.data)

from kiroku.web_crawler import get_webpage
from kiroku.db import log, insert_update, db
from kiroku.requester import get

ITEM_ROOT = "https://hacker-news.firebaseio.com/v0/item/"
TOP_ROOT = "https://hacker-news.firebaseio.com/v0/topstories.json"
NEW_ROOT = "https://hacker-news.firebaseio.com/v0/newstories.json"
BEST_ROOT = "https://hacker-news.firebaseio.com/v0/beststories.json"
MAX_ROOT = "https://hacker-news.firebaseio.com/v0/maxitem.json"


class HackerNews:
    """
    Encapsulate HackerNews the site
    """

    @staticmethod
    def get_max_id():
        r = get(MAX_ROOT)
        mid = int(r)
        log("hkns:max_id", {"id": mid})
        return mid

    @staticmethod
    def get_tops():
        r = get(TOP_ROOT)
        tops = r
        for story_id in tops:
            story = self.get_item(story_id)
            insert_update(story, "hkns")
        log("hkns:tops", {"tops": tops})
        return tops

    @staticmethod
    def get_news():
        r = get(NEW_ROOT)
        news = r
        log("hkns:news", {"news": news})
        return news

    @staticmethod
    def get_bests():
        r = get(BEST_ROOT)
        bests = r
        log("hkns:bests", {"bests": bests})
        return bests

    @staticmethod
    def get_item(item_id):
        """
        Get an item by id
        
        :param item_id: <int> ID of the item you want to get
        :return: <dict> Data about the item
        """
        url = "{}{}.json".format(ITEM_ROOT, item_id)
        data = get(url)
        data['_id'] = item_id
        return data


def scrape_hkns_items(base_id=None, limit=100):
    if not base_id:
        base_id = db['status'].find_one({"_id": "HN_max"})
        base_id = int(base_id['id'])
        print("Base_id {}".format(base_id))
    max_id = HackerNews.get_max_id()
    while max_id > base_id:
        base_id += 1
        item = HackerNews.get_item(base_id)
        if item["type"] == "story" and item.get("url"):
            get_webpage.delay(item["url"])
        insert_update(item, "HackerNews")
        print("Scrape item {}".format(item['_id']))
    db['status'].update_one({"_id": "HN_max"}, {"$set": {"id": max_id}}, upsert=True)



def scrape_hkns_metrics():
    insert_update({
        "tops": HackerNews.get_tops(),
        "bests": HackerNews.get_bests(),
        "max_id": HackerNews.get_max_id(),
        "type": "metrics"
    }, "hkns")

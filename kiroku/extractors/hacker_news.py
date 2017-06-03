from kiroku.db import log, insert_update
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
    def get_max_id(self):
        r = get(MAX_ROOT)
        mid = int(r)
        log("hkns:max_id", {"id": mid})
        return mid

    @staticmethod
    def get_tops(self):
        r = get(TOP_ROOT)
        tops = r
        for story_id in tops:
            story = self.get_item(story_id)
            insert_update(story, "hkns")
        log("hkns:tops", {"tops": tops})
        return tops

    @staticmethod
    def get_news(self):
        r = get(NEW_ROOT)
        news = r
        log("hkns:news", {"news": news})
        return news

    @staticmethod
    def get_bests(self):
        r = get(BEST_ROOT)
        bests = r
        log("hkns:bests", {"bests": bests})
        return bests

    @staticmethod
    def get_item(self, item_id):
        """
        Get an item by id
        
        :param item_id: <int> ID of the item you want to get
        :return: <dict> Data about the item
        """
        url = "{}{}.json".format(ITEM_ROOT, item_id)
        data = get(url)
        data['_id'] = item_id
        return data


def scrape_hkns_items(base_id, limit=100):
    pass


def scrape_hkns_metrics():
    insert_update({
        "tops": HackerNews.get_tops(),
        "bests": HackerNews.get_bests(),
        "max_id": HackerNews.get_max_id(),
        "type": "metrics"
    }, "hkns")

from hkns.config import db
import time
import requests



HEADERS = {
    "User-Agent": "Meow!"
}

ITEM_ROOT = "https://hacker-news.firebaseio.com/v0/item/"
TOP_ROOT = "https://hacker-news.firebaseio.com/v0/topstories.json"
NEW_ROOT = "https://hacker-news.firebaseio.com/v0/newstories.json"
BEST_ROOT = "https://hacker-news.firebaseio.com/v0/beststories.json"
MAX_ROOT = "https://hacker-news.firebaseio.com/v0/maxitem.json"


def log(event, data, col='log'):
    """
    A quick way to logged anything into mongoDB.
    Also insert time of the log if not already in the logged object.
    :param event: A type sort of of the log entry.
    :param data: The data to be logged.
    :parem col: Default to "log", the collection to store the log to.
    :return: None
    """
    logged = data
    try:
        logged["time"]
    except KeyError:
        logged["time"] = time.time()
    logged["event"] = event
    db[col].insert_one(logged)
    return


def max_id():
    r = requests.get(MAX_ROOT, headers=HEADERS)
    if r.status_code == 200:
        mid = int(r.text)
        db['raw'].insert_one({
            "id": mid,
            "time": time.time(),
            "type": "max_id",
        })
        return mid


def get_tops():
    r = requests.get(TOP_ROOT, headers=HEADERS)
    if r.status_code == 200:
        tops = r.json()
        db['raw'].insert_one({
            "bests": tops,
            "time": time.time(),
            "type": "top",
        })
        return tops


# We don't really need this.
def get_news():
    """
    Get the newest
    :return: 
    """
    r = requests.get(NEW_ROOT, headers=HEADERS)
    if r.status_code == 200:
        news = r.json()
        db['raw'].insert_one({
            "bests": news,
            "time": time.time(),
            "type": "new",
        })
        return news


def get_bests():
    r = requests.get(BEST_ROOT, headers=HEADERS)
    if r.status_code == 200:
        bests = r.json()
        db['raw'].insert_one({
            "bests": bests,
            "time": time.time(),
            "type": "best",
        })
        return bests


class HKitem:
    def __init__(self, _id):
        self._id = _id
        self.url = "{}{}.json".format(ITEM_ROOT, self._id)

    def get_data(self):
        """
        Issue a get request to get the item.
        :return: dict from the json respond
        """
        r = requests.get(self.url, headers=HEADERS)
        if r.status_code == 200:
            self.data = r.json()
            self.data['_id'] = self._id
            dd = db['items'].find_one({"_id": self._id})
            if dd:
                log("duplicate", {"id": self._id})
                return "Duplicate {}".format(self._id)
            else:
                db['items'].insert_one(self.data)
                log("insert", {"id": self._id})
                return "Inserted {}".format(self._id)
        else:
            log("error.request", {"status_code": r.status_code,
                                  "response_header": r.headers,
                                  "request": r.request})
            return "Error"

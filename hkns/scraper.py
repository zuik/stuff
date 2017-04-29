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


class HKitem:
    def __init__(self, id):
        self.id = id
        self.url = "{}{}.json".format(ITEM_ROOT, self.id)

    def get_data(self):
        """
        Issue a get request to get the item.
        :return: dict from the json respond
        """
        r = requests.get(self.url, headers=HEADERS)
        self.data = r.json()
        return self.data

    def get_item(self):
        """
        Create object base on the type of item.
        :return: A subclass of HKitem based on type
        """
        if not self.data:
            self.get_data()
        if self.data["type"] == "story":
            return HKstory(self.id, self.data)


class HKstory(HKitem):
    def __init__(self, id, data):
        HKitem.__init__(self, id)
        self.data = data

    def get_comments(self):
        # Get all the child comments
        pass

    def get_webpage(self):
        """
        Use requests to get the HTML of the url
        :return: String containing the HTML
        """
        # Get the page and store it in the item
        # TODO: Store this in a database backend
        # TODO: Parse just the text
        pass


if __name__ == "__main__":
    # Test get data
    a = HKitem(14223020)  # This is a story
    print(a.get_data())

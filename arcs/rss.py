import requests
from lxml import etree
from arcs.config import HEADERS


class RSS:
    def __init__(self, url):
        self.channel_info = None
        self.url = url
        self.root = None
        self.xml = None
        self.items = None

    def refresh(self):
        """
        Get the newest version of the XML
        
        :return: etree root element
        """
        r = requests.get(self.url, headers=HEADERS)
        if r.status_code == 200:
            self.root = etree.XML(r.content)
            return self.root
        else:
            raise Exception("Error on requesting the feed")

    def collect(self):
        print(self.url)
        # self.__init__(self.url)
        # self.refresh()
        # self.get_items()
        # self.get_channel_info()

    def get_items(self):
        """
        Parse all the items in the feed
        
        :return: list of item dicts
        """
        items = self.root.xpath("//item")
        r = []
        for item in items:
            title = item.xpath(".//title")[0].text
            description = item.xpath(".//description")[0].text
            link = item.xpath(".//link")[0].text
            publication_date = item.xpath(".//pubDate")[0].text
            r.append(
                {
                    "title": title,
                    "description": description,
                    "link": link,
                    "publication_date": publication_date,
                })
        self.items = r
        return self.items

    def get_channel_info(self):
        """
        Parse all the properties of the channel tag
        
        :return: dict with channel info
        """
        if not self.items:
            self.get_items()
        channel = self.root.xpath("//channel")[0]
        title = channel.xpath(".//title")[0].text
        link = channel.xpath(".//link")[0].text
        description = channel.xpath(".//description")[0].text
        self.channel_info = {
            "title": title,
            "link": link,
            "description": description,
            "items": self.items
        }
        return self.channel_info


if __name__ == '__main__':
    a = RSS("https://www.technologyreview.com/topnews.rss")
    a.refresh()
    print(a.get_items())
    print(a.get_channel_info())

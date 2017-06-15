import requests
from lxml import etree


class RSS:
    def __init__(self, url):
        self.url = url
        self.root = None
        self.xml = None

    def refresh(self):
        """
        Get the newest version of the XML
        :return: etree root element
        """
        r = requests.get(self.url, headers=HEADERS)
        return self.root
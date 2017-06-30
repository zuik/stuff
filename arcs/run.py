from arcs.rss import RSS
from arcs.controller import Controller

if __name__ == "__main__":
    ctr = Controller()
    mit_tech = RSS("https://www.technologyreview.com/topnews.rss")
    ctr.add_collector(mit_tech, 10)
    ctr.run()

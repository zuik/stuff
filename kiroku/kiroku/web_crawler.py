import hashlib

from kiroku.db import insert_update
from kiroku.extractors.hacker_news import scrape_hkns_items, scrape_hkns_metrics
from kiroku.requester import get
from kiroku.config import celery_app as app


@app.on_after_configure.connect
def setup(sender, **kwargs):
    sender.add_periodic_task(301.0, hkns.s())


@app.task(name="hkns")
def hkns():
    return scrape_hkns_items(), scrape_hkns_metrics()

@app.task(name="crawl_web")
def get_webpage(url):
    html = get(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"})
    _id = str(hashlib.sha1(html.encode("utf-8")).hexdigest())
    data = {
        "_id": _id,
        "html_data": html
    }
    insert_update(data, "webpages")

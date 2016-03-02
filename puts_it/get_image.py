from celery import Celery
import requests

BROKER_URL = 'redis://localhost:6379/0'
app_q = Celery(__name__, broker=BROKER_URL)

@app_q.task
def get(url):
    filename = url[url.find(".com/")+5:]
    img = requests.get(url)
    with open(filename, 'wb') as i: i.write(img.content)
    return filename

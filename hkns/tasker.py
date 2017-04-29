import time
from celery import Celery
from celery.schedules import crontab

app = Celery()

app.config_from_object('celeryconfig')


@app.on_after_configure.connect
def setup(sender, **kwargs):
    sender.add_periodic_task(600, get_items.s())


@app.task
def get_items():
    print("Hello")
    time.sleep(1)

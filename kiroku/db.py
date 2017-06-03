import time
from pymongo import MongoClient
from kiroku.config import MONGO_LOGIN

client = MongoClient(MONGO_LOGIN)
db = client['krk']


def insert_update(data, collection_name):
    """
    Insert if the item has unique _id else update the item.
    :param data: <dict> Data to be inserted into the database
    :param collection_name: <str> Collection name that the data should be inserted to
    :return: <bool> True if the insert is unique
    """
    col = db[collection_name]
    _id = data["_id"]
    cur = col.find_one({"_id": _id})
    if cur:
        log("update", {"id": _id, "previous": cur})
        col.replace_one({"_id": _id}, data)
        return False
    else:
        col.insert_one(data)
        return True


def log(event_type, data):
    """
    Log into the database
    :param event_type: <str> Type of the event
    :param data: 
    :return: 
    """
    db.insert_one({"eventType": event_type, "data": data, "time": time.time()})

import time
from pymongo import MongoClient
from kiroku.config import MONGO_LOGIN

client = MongoClient(MONGO_LOGIN)
db = client['krk']


def insert_update(data, collection_name):
    """
    Insert if the item has unique _id else update the item.
    
    :param dict data: Data to be inserted into the database
    :param str collection_name: Collection name that the data should be inserted to
    :return: True if the insert is unique
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


def find_by_id(_id, collection_name):
    """
    Fine *one* item by _id
    
    :param  ?  _id: The _id of the item
    :param  str collection_name: The name of the collection that you expect to find the item in. 
    :return: Data if found, else None
    """
    return db[collection_name].find_one({"_id": _id})


def log(event_type, data):
    """
    Log into the database
    
    :param str event_type: Type of the event
    :param dict data: 
    :return: 
    """
    db['log'].insert_one({"eventType": event_type, "data": data, "time": time.time()})

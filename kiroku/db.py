from pymongo import MongoClient
from kiroku.config import MONGO_LOGIN

client = MongoClient(MONGO_LOGIN)
db = client['krk']


def insert_update(data, collection_name, db=db):
    col = db[collection_name]
    _id = data["_id"]
    cur = col.find_one({"_id": _id})
    if cur:
        # log("update", {"id": _id, "previous": cur})
        col.update({"_id": _id}, data)
    else:
        col.insert_one(data)

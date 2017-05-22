from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

client = MongoClient("mongodb://zui:F0reverqwerty@localhost:27017/")
db = client['hkns3']


api = Flask(__name__)
CORS(api)
@api.route("/ts/<item_id>")
def ts_of_item(item_id):
    r = db['time_series2'].find_one({"id": int(item_id)})
    if r:
        return jsonify({ "rankings": r['ranking'], "times": r['times']})



if __name__ == "__main__":
    api.run(port=5001, debug=True)
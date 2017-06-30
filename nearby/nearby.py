from flask import Flask, request, render_template, Response
import json
import time
from bson.json_util import dumps
from pymongo import MongoClient
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_url_path='/static')
CORS(app)
client = MongoClient()
db = client['nearby']

# @app.route("/")
# def index_page():
#     return render_template('index.html')

@app.route("/msg", methods=['GET', 'POST'])
def handle_messages():
    if request.method == 'POST':
        message_post(request.data)
        # resp = Response(json.dumps({'status': 'ok'}))
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        # return resp
        return json.dumps({'status': 'ok'})
    else:
        # resp =  Response(get_message())
        # resp.headers['Access-Control-Allow-Origin'] = '*'
        # return resp
        return get_message()

def message_post(form_data):
    data = json.loads(form_data.decode("utf-8"))
    if data['location'] == None:
        location = None
    else:
        location = {
            "lat": data['location']['lat'],
            "lng": data['location']['lng'],
        }
    msg = {
        "content": data['text'],
        "time": time.time(),
#        "location":
    }
    db.msg.insert_one(msg)
    return

def get_message():
    msgs = [m for m in db.msg.find()]
    return dumps({'messages':msgs[::-1]})

if __name__=='__main__':
    app.run(ssl_context='adhoc')
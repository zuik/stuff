import youtube_dl
from pymongo import MongoClient
from flask import Flask, request
import time
import json

app = Flask(__name__)
ydl_opts={}
client = MongoClient()
db = client.rXive

@app.route("/")
def index():
    return "Hello, world"

@app.route("/getlink", methods=["POST","GET"])
def url_post_handle():
    if request.method == "POST":
        db.vidz.insert_one(get_link_from_url(request.form['url']))
        return str(request.form['url'])
    else:
        return "POST required"

def get_link_from_url(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        x = ydl.extract_info(url, download=False)
        d = {
            "vid_id":x['id'],
            "site":x['extractor'],
            "title":x['title'],
            "in_url":url,
            "dl_url":x['url'],
            "time":time.time(),
            "thumb_url":x['thumbnail']
        }
        return d

if __name__ == "__main__":
    app.run(debug=True)

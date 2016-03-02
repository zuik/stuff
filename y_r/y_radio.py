'''
Todo:
-User
'''

import json
import youtube_dl
import re
import time

from pymongo import MongoClient
from flask import Flask, request, render_template

app = Flask(__name__)
ydl_opts={}
client = MongoClient()
db = client.y_radio

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/get_links", methods=["POST","GET"])
def url_post_handle():
    if request.method == "POST":
        url_list = _process_post(request.form['urls'])
        url_list = [get_link_from_url(x) for x in url_list]
        url_list = [insert_to_db(y['_id'],y) for y in url_list]
        return index()
    else:
        return index()

@app.route("/listing")
def listing():
    url_listings = [x for x in db.vid.find()]
    return render_template("listing.html", urls = url_listings)

@app.route("/listen/<video_id>")
def listen(video_id):
	data = db.vid.find_one({"_id":video_id})
	audio_list =  data['audio_list']
	urls = []
	for audio in audio_list:
		if audio['ext'] == "webm":
			urls.append(audio)
	return render_template("player.html", urls = urls, data = data)

def _process_post(urls):
    url_list = urls.split("\n")
    return [_re_url(x) for x in url_list]
def _re_url(text):
    rs = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return rs.group(0) if rs else text
def insert_to_db(id, data):
    if not db.vid.find_one(id):
        return db.vid.insert_one(data)

def get_link_from_url(url):
    if not db.vid.find_one({'in_url':url}):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            x = ydl.extract_info(url, download=False)
            d = {
                "_id": x['extractor'] + ":" + x['id'],
                "vid_id":x['id'],
                "site":x['extractor'],
                "title":x['title'],
                "in_url":url,
                "dl_url":x['url'],
                "time":time.time(),
                "thumb_url":x['thumbnail'],
                "audio_list":[i for i in x['formats'] if i['format_note']=="DASH audio"],
                "json": json.dumps(x),
            }
            return d
    else:
        return db.vid.find_one({'in_url':url})

if __name__ == "__main__":
  app.run(debug = True)

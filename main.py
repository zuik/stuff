from flask import Flask, request, json
import youtube_dl
import time

ytpl = Flask(__name__)
ydl_opts = {
    "noplaylist": True
}

@ytpl.route("/videoinfo", methods=['GET', 'POST'])
def get_video_info():
    if request.method == 'GET':
        return json.jsonify({"error": "Please use POST"})
    if request.method == 'POST' and request.data or request.form:
        #payload = json.loads(request.data.decode("UTF-8"))
        url = json.loads(request.data.decode("utf-8"))
        if url:
            info = _get_info(url['url'])
            return json.jsonify(info)
        else: 
            return json.jsonify({"error": "Can't get information for this url'"})
    else:
        return json.jsonify({"error": "Undefined error"})

def _get_info(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        x = ydl.extract_info(url, download=False)
        x['original_url'] = url
        x['system_time'] = time.time()
 #       x['audio_list'] = [i for i in x['formats'] if i['format_note']=="DASH audio"]
        return x


if __name__ == "__main__":
    ytpl.run(debug = True)
import json
from youtube_dl import YoutubeDL

ydl_opts = {
    "noplaylist": True  # For now, we will seperate playlist and singles later
}


def get_info(url):
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info


def audio_urls(url):
    # info = get_info(url)
    info = load_test_json('/Users/zui/kode/python/yufonium/yufonium/test_result.json')
    audio_tracks = [i for i in info['formats'] if i['format_note'] == "DASH audio"]
    return [{'format': i['format'], 'url': i['url'], 'filesize': i['filesize']} for i in audio_tracks]


def load_test_json(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)

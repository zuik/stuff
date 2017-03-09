import json
from youtube_dl import YoutubeDL

ydl_opts = {
    "noplaylist": True  # For now, we will seperate playlist and singles later
}


def get_info(url):
    print("Getting info for {}".format(url))
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info


def audio_urls(info):
    """
    Extract the audio urls from the JSON blob that youtube_dl spits out
    :param info: The JSON blob that youtube_dl spits out
    :return: A list of tuples (filesize, format_id, url, ext ) of audio urls sorted by filesize
    """
    # info = get_info(url)
    # info = load_test_json('/Users/zui/kode/python/yufonium/yufonium/test_result.json')
    audio_tracks = [i for i in info['formats'] if i['format_note'] == "DASH audio"]
    print("Got {} tracks".format(len(audio_tracks)))
    # Todo: Convert this to named tuple
    return sorted([(i['filesize'],
                    i['format_id'],
                    i['url'],
                    i['ext'],
                    ) for i in audio_tracks], key=lambda x: x[0])


def load_test_json(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


if __name__ == "__main__":
    # Test get audio url
    print(audio_urls("blah"))

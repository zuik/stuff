import json
from youtube_dl import YoutubeDL

ydl_opts = {
    "noplaylist": True  # For now, we will separate playlist and singles later
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


# Todo: Extract this to seperate functionality, for testing later
def load_test_json(filename):
    with open(filename, 'r') as f:
        data = f.read()
        return json.loads(data)


def save_test_json(filename, data):
    with open(filename, 'wb') as f:
        f.write(data.encode("utf-8"))
        return filename


# Todo: Merge this with the original extract method.
# There is no point to seperate this out.
# The only different of from the other extract method is that
# this doesn't have the extract playlist option.

# Another problem with this is that
# if in the playlist there is a video which has problem,
# youtube_dl will throw an error.
# Todo: Playlist error handling
def extract_playlist(url):
    with YoutubeDL({}) as ydl:
        info = ydl.extract_info(url, download=False)
        return info



if __name__ == "__main__":
    pass
    # Test get audio url
    # print(audio_urls("blah"))

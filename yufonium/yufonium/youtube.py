import json
import re

from youtube_dl import YoutubeDL
from youtube_dl.extractor.youtube import YoutubePlaylistIE
from yufonium.utils import save_test_json

ytplie = YoutubePlaylistIE()

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

# Todo: Merge this with the original extract method.
# There is no point to seperate this out.
# The only different of from the other extract method is that
# this doesn't have the extract playlist option.

def extract_playlist(url):
    with YoutubeDL({"ignoreerrors": True}) as ydl:
        info = ydl.extract_info(url, download=False)
        return info


def is_playlist(url):
    """
    Check if playlist
    :param url: Url from the user
    :return: playlist_id or False
    """
    match = re.match(ytplie._VALID_URL, url)
    if not match:
        return False
    playlist_id = match.group(1) or match.group(2)
    return playlist_id


if __name__ == "__main__":
    # Test playlist download
    # This url has video id in it
    url = "https://www.youtube.com/watch?v=mezYFe9DLRk&list=PLYxjne28x-DlSRzO8yvMwmCTyGBrVAhka"
    print(is_playlist(url))
    url = "https://www.youtube.com/playlist?list=PLYxjne28x-DlSRzO8yvMwmCTyGBrVAhka"
    print(is_playlist(url))
    url = "https://www.youtube.com/watch?v=mezYFe9DLRk"
    print(is_playlist(url))
    # save_test_json("test.json", json.dumps(extract_playlist(url)))

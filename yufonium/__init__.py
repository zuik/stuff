from yufonium.youtube import get_info, audio_urls
from yufonium.downloader import download
import json


def download_audio(url):
    """
    Uses youtube_dl to get info about the video and download the audio using requests
    :param url: YouTube's video url (include http:// )
    :return: (filename, info)
    """
    info = get_info(url)
    files = audio_urls(info)
    # We will download the largest file in the list
    file = files[-2]
    filename = download(file[2], "{}_{}.{}".format(info['id'], file[1], file[3]))
    return (filename, info)


if __name__ == '__main__':
    # url = 'https://www.youtube.com/watch?v=cLfyjIlu9Uw'
    # print(json.dumps(get_info(url)))
    # print(audio_urls("test"))
    # Test downloader from init
    # print(download("https://images7.alphacoders.com/782/thumb-1920-782943.png", "konosuba_wall.png"))
    download_audio('https://www.youtube.com/watch?v=cLfyjIlu9Uw')

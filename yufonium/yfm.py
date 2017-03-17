from yufonium.youtube import is_playlist
class Yufonium(object):
    """
    A video or a playlist for us to dissect
    """
    def __init__(self, url):
        self.url = url
        self.playlist = is_playlist(url)
    def download_info(self):
        pass

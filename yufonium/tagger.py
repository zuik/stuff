# For now, we will use the limited version of ID3v2.
# This doesn't let us insert the picture however :(
# Todo: Non-easy ID3

from mutagen.easyid3 import EasyID3


def insert_info(filename, info):
    f = EasyID3(filename)
    f['title'] = info['title']
    f.save()

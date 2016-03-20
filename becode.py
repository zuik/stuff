"""
This module handle the decoding and encoding of torrent's bencode.
The source of bencode could be passed in through a file or a bytes string.
It is nice to stop at decode. Formatting is purely a decoration on top of
the bytes dict result from the bencoded file
"""

import binascii

ENCODING = "UTF-8" #In case we are crazy

class TorrentFile(object):
    """
    I can't think of a better name for this class.
    """
    def __init__(self, file=None, text=None):
        """
        Create a decoder/encoder.
        Please don't try to use both file and text.
        But if you do, it will favour file.
        :param file: Path to the bencoded torrent file.
        :param text: A bencoded bytes string. This is mostly use for convinence during testing.
        :return:
        """
        if file:
            with open(file, 'rb') as f:
                self.text = f.read()
        elif text:
            self.text = text
        self.decoded = None
        self.formatted = None
    def decode(self):
        if not self.decoded:
            self.decoded = decode(self.text)
        return self.decoded
    def format(self):
        if not self.formatted:
            self.formatted = format_bencode(self.decoded)
        return self.formatted

def decode(text):
    """
    The way decode work is similar to the original bencode module.
    decode recursively walk through the text and gradually decode them.
    In its helper functions, the return contain the decoded text along
    with the undecoded remain of the text. The condition attached to
    each return was there to get rid of the empty byte when the final
    result are return.
    :param text: A bencoded bytes string
    :return: A Pythonic (?) interpretation of that bytes string
    """
    head = text[0:1]
    if head == b'l':
        return _decode_list(text)
    if head == b'i':
        return _decode_int(text)
    if head == b'd':
        return _decode_dict(text)
    if head in [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9']:
        return _decode_str(text)

def _decode_str(text):
    colon = text.index(b":") + 1
    length = int(text[:colon-1].decode())
    value, text = text[colon:(colon+length)], text[colon+length:]
    return (value, text) if len(text) > 0 else value

def _decode_int(text):
    length = text.index(b"e")
    value, text = text[1:length], text[length+1:]
    return (value, text) if len(text) > 0 else value

def _decode_list(text):
    text = text[1:]
    r = []
    while True:
        value, text = decode(text)
        r.append(value)
        if text[0:1] == b"e":
            return (r, text[1:]) if len(text) > 1 else r
            break

def _decode_dict(text):
    text = text[1:]
    r = {}
    while True:
        key, text = _decode_str(text)
        value, text = decode(text)
        r[key] = value
        if text[0:1] == b"e":
            return (r, text[1:]) if len(text) > 1 else r
            break

def format_bencode(text):
    """
    I was worry that format is not a good name to name this function.
    Anyway, it is just to convert the bencode to something more sane.
    The only interesting thing to note is that for a valid torrent file
    only the key ['pieces'] is special. Most other you could decode them as string,
    but since ['pieces'] contains SHA-1 hashes of the pieces, it would yell at you
    if you tried to decode it as UTF-8 or something.
    Therefore, for ['pieces'], it is interpret as a list of SHA-1 hash instead. That
    might be helpful later on.
    :param text: The *decoded* bencode.
    :return: A sane interpretation of the original bencode
    """
    if isinstance(text, dict):
        return _format_dict(text)
    elif isinstance(text, list):
        return _format_list(text)
    elif isinstance(text, bytes):
        return _format_str(text)

def _format_str(text):
    try:
        return int(text)
    except ValueError:
        return text.decode(ENCODING)

def _format_list(text):
    r = []
    for value in text:
        r.append(format_bencode(value))
    return r

def _format_dict(text):
    r = {}
    for key, value in text.items():
        if key == b'pieces':
            r['pieces'] = _format_pieces(value)
        else:
            key = _format_str(key)
            value = format_bencode(value)
            r[key] = value
    return r
def _format_pieces(text):
    r = [x for x in _cut_pieces(text, 20)]
    r = [binascii.hexlify(x).decode(ENCODING) for x in r]
    return r

def _cut_pieces(text, pieces_size):
    for i in range(0, len(text), pieces_size):
        yield text[i:i+pieces_size]

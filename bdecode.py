def decode_string(text):
    colon = text.index(b":") + 1
    length = int(text[:colon-1].decode())
    value, text = text[colon:(colon+length)], text[colon+length:]
    return (value, text) if len(text) > 0 else value

def decode_int(text):
    length = text.index(b"e")
    value, text = text[1:length], text[length+1:]
    return (value, text) if len(text) > 0 else value

def decode_list(text):
    text = text[1:]
    r = []
    while True:
        value, text = decode(text)
        r.append(value)
        if text[0:1] == b"e":
            return (r, text[1:]) if len(text) > 1 else r
            break

def decode_dict(text):
    text = text[1:]
    r = {}
    while True:
        key, text = decode_string(text)
        value, text = decode(text)
        r[key] = value
        if text[0:1] == b"e":
            return (r, text[1:]) if len(text) > 1 else r
            break

def decode(text):
    head = text[0:1]
    if head == b'l':
        return decode_list(text)
    if head == b'i':
        return decode_int(text)
    if head == b'd':
        return decode_dict(text)
    if head in [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9']:
        return decode_string(text)

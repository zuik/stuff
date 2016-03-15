def decode_string(text):
    colon = text.index(b":")
    length = int(text[:colon].decode())
    try:
        ended = text[length+1:] == b'e'
    except IndexError:
        ended = False
    return (#length,
            text[colon+1:(colon+1+length)],
            text[colon+1+length:],
            #ended,
    )

def decode_int(text):
    length = text.index(b"e")
    try:
        ended = text[length+1:] == b'e'
    except IndexError:
        ended = False
    return (int(text[1:length]),
            text[length+1:],
            #ended
           )
def decode_list(text):
    text = text[1:]
    r = []
    ended = False
    n = 100
    while n>0:
        #print(text)
        value, rest = decode(text)
        r.append(value)
        text = rest
        #print(value, rest, n)
        n -= 1
        if rest[0:1] == b"e":
            #print(r, rest)
            return r, rest[1:]
            break
def decode_dict(text):
    text = text[1:]
    r = {}
    n = 100
    while n>0:
        n -= 1
        key, rest = decode_string(text)
        text = rest
        #print(rest, key)
        value, rest = decode(text)
        text = rest
        r[key] = value
        if rest[0:1] == b"e":
            #print(r, rest)
            return r, rest[1:]
            break
        #print(value, rest, key)
def decode(text):
    pointer = text[0:1]
    #print(pointer)
    if pointer == b'l':
        return decode_list(text)
    if pointer == b'i':
        #print(text[1:])
        return decode_int(text)
    if pointer == b'd':
        return decode_dict(text)
    if pointer in [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9']:
        return decode_string(text)

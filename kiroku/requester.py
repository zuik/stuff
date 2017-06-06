import requests

from kiroku.config import HEADERS
from kiroku.db import log


def get(url, params=None, headers=HEADERS):
    """
    Issue a GET request and return the response
    
    :return: <dict> JSON parsed from the response
    """
    r = requests.get(url, params=params, headers=headers)
    if r.status_code == 200:
        try:
            return r.json()
        except:
            return r.text
    else:
        log("error", {"type": "request error", "statusCode": r.status_code, "resp": r.content})
        raise Exception("Request error", "Status code: {}".format(r.status_code))

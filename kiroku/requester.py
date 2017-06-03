from kiroku.config import HEADERS
from kiroku.db import log


def _get(url, params, headers=HEADERS):
    """
    Issue a GET request and return the response
    :return: <dict> JSON parsed from the response
    """
    r = requests.get(url, params=params, headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        log("error", {"type": "request error", "statusCode": r.status_code, "resp": r.content})

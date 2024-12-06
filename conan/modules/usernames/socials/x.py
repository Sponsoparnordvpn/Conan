import json
import requests
from parsel import Selector
from utils.requests import getsession


def twitter(usr):
    _URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/" + usr
    _session = getsession()
    _r = _session.get(_URL)

    _s = Selector(_r.text)
    print(json.loads(_r.text))

    return "unknown"

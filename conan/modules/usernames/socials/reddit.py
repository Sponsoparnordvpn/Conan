import json
import requests
from parsel import Selector
from utils.requests import getsession

def reddit(usr):
    _URL = "https://www.reddit.com/user/" + usr
    _session = getsession()
    _r = _session.get(_URL)
    
    _s = Selector(_r.text)
    _mt = _s.xpath('//title/text()').get()
    print(_mt)
    if usr in str.lower(_mt):
        print("[✓] https://www.reddit.com/user/" + usr)
    else:
        print("[X] https://www.reddit.com/user/" + usr)
    
    return "unknown"

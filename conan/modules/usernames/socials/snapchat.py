import json
import requests
from parsel import Selector
from utils.requests import getsession

def snapchat(usr):
    _URL = "https://www.snapchat.com/add/" + usr
    _session = getsession()
    _r = _session.get(_URL)
    
    _s = Selector(_r.text)
    _mt = _s.xpath('//meta[@property="og:description"]/@content').get()
    if _mt and _r.status_code == 200:
        print("[✓] https://www.snapchat.com/add/" + usr)
    else:
        print("[X] https://www.snapchat.com/add/" + usr)
    
    return "unknown"

import json
import requests
from parsel import Selector
from utils.requests import getsession

def tiktok(usr):
    _URL = "https://tiktok.com/@" + usr
    _session = getsession()
    _r = _session.get(_URL)
    
    selector = Selector(_r.text)
    data = selector.xpath("//script[@id='__UNIVERSAL_DATA_FOR_REHYDRATION__']/text()").get()

    try:
        profile_data = json.loads(data)["__DEFAULT_SCOPE__"]["webapp.user-detail"]
        if not profile_data.get("userInfo"):
            print("[X] https://tiktok.com/@" + usr)
        else:
            print("[✓] https://tiktok.com/@" + usr)
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        print("[?] https://tiktok.com/@" + usr)
    
    return "unknown"


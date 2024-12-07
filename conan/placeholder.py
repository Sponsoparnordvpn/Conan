import json
import requests
from parsel import Selector
from utils.config import *
from utils.requests import getsession

def tiktok(usr, debug):
    _URL = "https://tiktok.com/@" + usr
    _session = getsession()
    _r = _session.get(_URL)
    
    selector = Selector(_r.text)
    data = selector.xpath("//script[@id='__UNIVERSAL_DATA_FOR_REHYDRATION__']/text()").get()

    try:
        profile_data = json.loads(data)["__DEFAULT_SCOPE__"]["webapp.user-detail"]
        print(profile_data)
        if not profile_data.get("userInfo"):
            dprint("[X] https://tiktok.com/@" + usr, debug)
        else:
            dprint("[✓] https://tiktok.com/@" + usr, debug)
    except (KeyError, TypeError, json.JSONDecodeError) as e:
        dprint("[?] https://tiktok.com/@" + usr, debug)
    
    return "unknown"


print(tiktok("spxnso", False))
import json
import requests
from parsel import Selector
from utils.requests import getsession
from utils.config import *


def snapchat(usr, debug):
    _URL = "https://www.snapchat.com/add/" + usr
    _session = getsession()
    _r = _session.get(_URL)
    
    _s = Selector(_r.text)
    _mt = _s.xpath('//meta[@property="og:description"]/@content').get()
    if _mt and _r.status_code == 200:
        dprint("[✓] https://www.snapchat.com/add/" + usr, debug)
        return True
    else:
        dprint("[X] https://www.snapchat.com/add/" + usr, debug)
        
    return "unknown"

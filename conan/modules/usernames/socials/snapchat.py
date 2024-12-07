from html import unescape
import json
import re
import requests
from parsel import Selector
from utils.requests import getsession
from utils.config import *


def snapchat(usr, debug):
    _URL = "https://www.snapchat.com/add/" + usr
    _session = getsession()
    _r = _session.get(_URL)
    _s = Selector(_r.text)
    _json = _s.xpath('//script[@type="application/ld+json"]/text()').get()
    if _json and _r.status_code == 200:
        try:
            cj = unescape(_json)
            cj = re.sub(r"[\n\r]", " ", cj)
            data = json.loads(cj)
            data["mainEntity"]["cuttedImage"] = _s.xpath('//meta[@property="og:image"]/@content').get()
            dprint("[✓] https://www.snapchat.com/add/" + usr, debug)
            return data
        except json.JSONDecodeError as e:
            dprint(f"[~] https://www.snapchat.com/add/{usr}", debug)
            return "nodata"
    else:
        dprint("[X] https://www.snapchat.com/add/" + usr, debug)
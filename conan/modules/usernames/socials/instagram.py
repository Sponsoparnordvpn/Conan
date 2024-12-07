import json
from parsel import Selector
from utils.requests import getsession
from utils.config import *
from html import unescape
import re
def instagram(usr, debug):
    _session = getsession()
    _URL = f"https://imginn.com/{usr}"
    _r = _session.get(_URL)
    _s = Selector(_r.text)
    
    _json = _s.xpath('//script[@type="application/ld+json"]/text()').get()
    if _json:
        try:
            cj = unescape(_json)
            cj = re.sub(r"[\n\r]", " ", cj)
            data = json.loads(cj)
            dprint(f"[✓] https://instagram.com/{usr}", debug)
            return data
        except json.JSONDecodeError as e:
            dprint(f"[~] https://instagram.com/{usr}", debug)
            return "nodata"
    else:
        dprint(f"[X] https://instagram.com/{usr}", debug)
        return



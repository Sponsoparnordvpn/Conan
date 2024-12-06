from parsel import Selector
import requests
from utils.requests import getsession
from utils.config import *

def instagram(usr, debug):
    _session = getsession()
    _URL = "https://instagram.com/" + usr
    _session.headers.update({"User-Agent": "Mozilla/5.0 "}) # Instagram was not accepting my randomly generated user agents..
    _r = _session.get(_URL)
    _s = Selector(_r.text)

    _mt = _s.xpath('//meta[@name="description"]/@content').get() # @property="og:description"/@property="og:title"/@name="description"/@property="og:image"

    if _mt:
        #print(f"Content: {_mt}")

        #parsed_data = _mt.split()
        #print(f"Parsed Data: {parsed_data}")
        dprint("[✓] https://instagram.com/" + usr, debug)
        return True
    else:
        dprint("[X] https://instagram.com/" + usr, debug)

    return "unknown"

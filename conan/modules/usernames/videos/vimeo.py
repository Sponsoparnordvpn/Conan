from parsel import Selector
import requests
from utils.config import *
from utils.requests import getsession


def vimeo(usr, debug):
    _URL = f"https://vimeo.com/{usr}"
    _session = getsession()
    _r = _session.get(_URL)
    _s = Selector(_r.text)
    _mt = _s.xpath('//meta[@property="og:title"]/@content').get()
    if _mt:
        dprint("[✓] https://vimeo.com/@"+usr, debug)
        return True
    else:
        dprint("[X] https://vimeo.com/@"+usr, debug)

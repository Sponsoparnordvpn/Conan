# I should honestly thank Scrapetube for the cookie acceptance, I was lost :sob:
from parsel import Selector
import requests
from utils.config import *
from utils.requests import getsession


def youtube(usr, debug):
    _URL = f"https://www.youtube.com/@{usr}/videos?view=0&flow=grid"
    _session = getsession()
    _session.cookies.set("CONSENT", "YES+cb", domain=".youtube.com")
    _r = _session.get(_URL, params={"ucbcb": 1})
    _s = Selector(_r.text)
    _mt = _s.xpath('//meta[@property="og:title"]/@content').get()
    if _mt:
        dprint("[✓] https://www.youtube.com/@"+usr, debug)
        return True
    else:
        dprint("[X] https://www.youtube.com/@"+usr, debug)


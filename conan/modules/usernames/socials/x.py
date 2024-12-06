import json
import requests
from parsel import Selector
from utils.config import *
from utils.requests import getsession


def twitter(usr, debug):
    _URL = "https://syndication.twitter.com/srv/timeline-profile/screen-name/" + usr
    _session = getsession()
    _r = _session.get(_URL)

    _s = Selector(_r.text)
    _script = _s.xpath('//script[@id="__NEXT_DATA__"]/text()').get()
    if _script:
        _data = json.loads(_script)
        if _data['props']['pageProps']['contextProvider']['hasResults']:
            dprint("[✓] https://www.x.com/" + usr, debug)
            return True
        else:
            dprint("[X] https://www.x.com/" + usr, debug)
            return False
    else:
        dprint("[?] https://www.x.com/" + usr, debug)
        return "unknown"

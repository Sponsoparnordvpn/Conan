import json
import requests
from parsel import Selector
from utils.config import *
from utils.requests import getsession


def reddit(usr, debug):

    _URL = f"https://gateway.reddit.com/desktopapi/v1/user/{usr}/posts?rtj=only&allow_over18=1&include=identity&after=0&dist=25&sort=new&t=all" # posts
    _CURL = f"https://gateway.reddit.com/desktopapi/v1/user/{usr}/conversations?rtj=only&allow_over18=1&include=identity&after=1&dist=25&sort=new&t=all"
    _session = getsession()
    _r = _session.get(_URL)
    _rc = _session.get(_CURL)

    _data = _r.json()
    if _data.get("authorFlair") != None:
        dprint("[✓] https://www.reddit.com/user/" + usr, debug)
        return _data
    else:
        dprint("[X] https://www.reddit.com/user/" + usr, debug)

    
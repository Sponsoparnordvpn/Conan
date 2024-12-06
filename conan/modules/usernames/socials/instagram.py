from parsel import Selector
import requests
from utils.requests import getsession


def instagram(usr):
    _session = getsession()
    _URL = "https://instagram.com/" + usr
    _session.headers.update({"User-Agent": "Mozilla/5.0 "}) # Instagram was not accepting my randomly generated user agents..
    _r = _session.get(_URL)
    _s = Selector(_r.text)

    _mt = _s.xpath('//meta[@property="og:title"]/@content').get()

    if _mt:
        # print(f"Content: {_mt}")

        # parsed_data = _mt.split()
        # print(f"Parsed Data: {parsed_data}")
        print("[✓] https://instagram.com/" + usr)
    else:
        print("[X] https://instagram.com/" + usr)

    return "unknown"

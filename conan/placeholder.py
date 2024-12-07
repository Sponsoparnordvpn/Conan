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
            cleaned_json = unescape(_json)
            cleaned_json = re.sub(r"[\n\r]", " ", cleaned_json)
            parsed_data = json.loads(cleaned_json)
            print("Parsed Data:", json.dumps(parsed_data, indent=2))
        except json.JSONDecodeError as e:
            dprint(f"[!] JSON parsing error: {e}", debug)
            dprint(f"Original JSON: {_json}", debug)
            return "json_parse_error"
    else:
        dprint(f"[!] No JSON data found on {_URL}", debug)
        return "no_json"

    return "success"

instagram("maxence_xoxo", False)

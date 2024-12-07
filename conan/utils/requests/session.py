import requests
import cloudscraper
from .headers import generate

_session = cloudscraper.CloudScraper() # Will bypass cloudflare's anti bot techniques
_session.headers.update(generate())

def getsession():
    return _session
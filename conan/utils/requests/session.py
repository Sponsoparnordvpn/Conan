import requests
from .headers import generate

_session = requests.Session()
_session.headers.update(generate())

def getsession():
    return _session
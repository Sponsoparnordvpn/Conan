# I didn’t want to scrape using a headless browser; however, I couldn’t find a solution to bypass the cookie acceptance dialog.
# so yeah gotta use selenium for that 1
from parsel import Selector
import requests



def youtube(usr):
    _URL = "https://youtube.com/@" + usr
    
    _r = requests.get(_URL, generator())
    
    if _r.status_code == 200:
        _s = Selector(_r.text)
        _mt = _s.xpath('//meta[@property="og:title"]/@content').get()
        print(_mt)
        title = _s.xpath('//title/text()').get() 
        print(f"Page Title: {title}")
    else:
        print(f"Failed to fetch page. Status code: {_r.status_code}")

youtube("ezkopzioezo")

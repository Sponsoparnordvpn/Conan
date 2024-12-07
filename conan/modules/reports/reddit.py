import json
import datetime

def rgen(data):
    if data == None:
        return
    posts = data["posts"]
    subreddits = data["subreddits"]
    pposts = {}
    ssubs = {}
    for post in posts:
        post = posts[post]
        pdata = {
            "title": post["title"],
            "author": post["author"],
            "thumbnail": post["thumbnail"]["url"],
            "identifier": post["postId"],
            "createdAt": datetime.datetime.utcfromtimestamp(post.get("created", 0) / 1000).isoformat(),
            "score": post["score"],
            "isLocked": post["isLocked"],
        }
        pposts[post["postId"]] = pdata
    for subreddit in subreddits:
        subreddit = subreddits[subreddit]
        sdata = {
            "name": subreddit["name"],
            "title" : subreddit["title"],
            "type" : subreddit["type"],
            "icon": subreddit["communityIcon"],
            "subscribers": subreddit["subscribers"],
            "isNSFW": subreddit["isNSFW"]
        }
        ssubs[subreddit["id"]] = sdata
        
    
    data = {
        "type": "reddit", 
        "username": "username", 
        "posts": pposts,
        "subreddits": ssubs,
        "comments": {}
    }
    return json.dumps(data, indent=4)

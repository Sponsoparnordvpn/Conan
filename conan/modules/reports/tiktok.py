import json


def tgen(data):
    if data is None:
        return
    data = {
        "type": "tiktok",
        "profile": {
            "avatar": data["userInfo"]["user"]["avatarLarger"],
            "mediumavatar": data["userInfo"]["user"]["avatarMedium"],
            "name": data["userInfo"]["user"]["nickname"],
            "username": data["userInfo"]["user"]["uniqueId"],
        },
        "stats": {
            "follower_count": data["userInfo"]["stats"]["followerCount"],
            "following_count": data["userInfo"]["stats"]["followingCount"],
            "heart_count": data["userInfo"]["stats"]["heartCount"],
            "video_count": data["userInfo"]["stats"]["videoCount"],
        },
        "bio": data["userInfo"]["user"]["signature"],
        "region": data["userInfo"]["user"]["region"],
        "verified": data["userInfo"]["user"]["verified"],
    }
    return json.dumps(data, indent=4)

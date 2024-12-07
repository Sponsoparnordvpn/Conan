import json


def igen(data):
    if data == None:
        return
    data = {
        "type": "instagram",
        "profile": {
            "pfp": data["mainEntity"]["image"],
            "name": data["mainEntity"]["name"],
            "username": data["mainEntity"]["alternateName"],
            "identifier": data["mainEntity"]["identifier"],
            "description": data["mainEntity"]["description"],
            "followers": next(
                (
                    stat["userInteractionCount"]
                    for stat in data["mainEntity"]["interactionStatistic"]
                    if stat["interactionType"] == "https://schema.org/FollowAction"
                ),
                0,
            ),
            "likes": next(
                (
                    stat["userInteractionCount"]
                    for stat in data["mainEntity"]["interactionStatistic"]
                    if stat["interactionType"] == "https://schema.org/LikeAction"
                ),
                0,
            ),
        },
        "posts" : {
            
        }
    }
    return json.dumps(data, indent=4)


import json


def sgen(data):
    if data == None:
        return
    data = {
        "type": "snapchat",
        "profile": {
            "bitmoji": data["mainEntity"]["image"],
            "cuttedBitmoji": data["mainEntity"]["cuttedImage"],
            "name": data["mainEntity"]["name"],
            "username": data["mainEntity"]["alternateName"],
        },
    }
    return json.dumps(data, indent=4)

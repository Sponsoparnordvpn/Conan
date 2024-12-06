import json
import os


def parseconfig():
    with open("config.json", "r") as f:
        return json.load(f)

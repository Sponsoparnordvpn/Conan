import json
import pyperclip
from utils.config.parser import parseconfig
from tests.benchmark.requests.socials import *
from modules.usernames import *
from modules.reports import ggen, igen, sgen, tgen, rgen

_CNT = 180
_WM = r"""
 _____                          
/  __ \                         
| /  \/ ___  _ __   __ _ _ __   
| |    / _ \| '_ \ / _` | '_ \  
| \__/\ (_) | | | | (_| | | | | 
 \____/\___/|_| |_|\__,_|_| |_| 
                                
"""

print(_WM)

print("----------------------------------------------")
print("Author: spxnso")
print("Version: 1.0.0")
print("----------------------------------------------")
print("Options:\n 1.Username Search\n 5.Benchmark\n 6.Configuration")

_OPT = int(input("Select an option: "))

if _OPT == 1:
    _USER = str(input("Enter an username: "))
    print("Searching on " + str(FC) + " websites for the username: " + _USER)
    _igC = instagram(_USER, False)
    _tC = tiktok(_USER, False)
    _sC = snapchat(_USER, False)
    twitter(_USER, False)
    _rC = reddit(_USER, False)
    youtube(_USER, False)
    vimeo(_USER, False)
    detail = (
        input("Would you like to get a detailled report about that user? (yes/no): ")
        .strip()
        .lower()
    )
    if "y" in detail:
        print("Generating the report...")
        _igR = igen(_igC)
        _sC = sgen(_sC)
        _tC = tgen(_tC)
        _rC = rgen(_rC)
        r = (
            input("Report succesfully generated, would you like to save it? (yes/no): ")
            .strip()
            .lower()
        )
        if "y" in r:
            content = ggen(_igR, _sC, _tC, _rC)
            print("Succesfully saved the report.")
            ar = (
                input(
                    "Would you like to generate an AI prompt? (yes/no): "
                )
                .strip()
                .lower()
            )
            if "y" in ar:
                pyperclip.copy(f"Hello, could you please create a resume in .md format based on the following data? Please include some educated guesses, such as the person's age based on descriptions, images, profile pictures (pfps), bitmojis, etc. Make sure to clearly mark the information that is guessed. If you think some information may not be related to the user (for example, if someone else is using the same username), please mention it:\n{content}")
                print("Prompt succesfully set to the clipboard")
elif _OPT == 5:
    print("Conan 1.0.0 Benchmark tool is a tool to check for any potential errors.")
    print("Starting the benchmark...")
    benchmark()
elif _OPT == 6:
    confirm = (
        input(
            "This option will reconfigure your Conan entirely. Are you sure? (yes/no): "
        )
        .strip()
        .lower()
    )
    if "y" in str.lower(confirm):
        while True:
            c = (
                input(
                    "Would you like to use requests or a headless browser? (requests/headless/why): "
                )
                .strip()
                .lower()
            )
            if "requests" in c:
                config = parseconfig()
                config["type"] = c
                with open("config.json", "w") as f:
                    json.dump(config, f, indent=4)
                print("Successfully set the type of searches to requests")
                break
            elif "headless" in c:
                with open("config.json", "r") as f:
                    config = json.load(f)
                    config["type"] = c
                with open("config.json", "w") as f:
                    json.dump(config, f, indent=4)
                print("Successfully set the type of searches to a headless browser")
                break
            elif "why" in c:
                print(
                    "1. Using requests will yield faster results; however, some websites may not be available.\n"
                    "2. Using a headless browser will lead to slower performance; however, all websites are available."
                )
            else:
                print("Invalid input. Please type 'requests', 'headless', or 'why'.")
    elif "n" in str.lower(confirm):
        print("Operation canceled.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

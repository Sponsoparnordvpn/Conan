from socials.instagram import instagram

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
print("Options:\n 1.Username Search\n")

_OPT = int(input("Select an option: "))

if _OPT == 1:
    _USER = str(input("Enter an username: "))
    print("Searching on "+str(_CNT)+" websites for the username: "+_USER)
    instagram(_USER)
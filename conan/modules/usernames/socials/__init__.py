import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from .instagram import instagram
from .tiktok import tiktok
from .snapchat import snapchat
from .reddit import reddit
COUNT = 5
# # coding: utf-8

# ### lib ###
import requests
import datetime  
import json
import random
import hmac
from hashlib import sha1
import base64
import time
import sys
import os
import re
import configparser as ConfigParser
from math import sin, cos, sqrt, atan2, radians
import ast
import sqlite3 as sqlite
import uuid
from oauth2client.service_account import ServiceAccountCredentials
import gspread

## information ##
GLOBAL = {
    "FILE_ROUTE": '%s/' % os.path.dirname(os.path.abspath(__file__)),
    "LINE_TOKEN": 'vZwZvgmlljz+VfSYn6Khu2RXQM8Gq3gkODZD8tdHEYgcxsUCI3rHSgh3CO3d7xmXvZ8irnEBQxm1Wughpaj+u1qANpzBavf3VTczraBo+VE4n4QaQpuhGwro/4wMXS1Zde+CyZ0d2Bxk55ZQG4MZBAdB04t89/1O/w1cDnyilFU=',
    "LINE_SECRET": 'c56fe3888c3cfe60a1969fdd19c9b10c',
    "APP_ID": 'ad64f3b34d38425ca0bb7efdcdb4548b',
    "APP_KEY": 'wabKRdVqcFg4i5CqLXP4JuWQ3Ws',
    "GOOGLE_MAP_KEY": 'AIzaSyCUx_og-8aUvdj5jDYyQGALwnzlQw_jXok',
    "IMAGE_URL": "https://worldcrater.com/Ahfargo_bus_bot_image/",
    "RICH_FUNC": "richmenu-ce2919554f6ff106c075bef379923fab",
    "RICH_INFO": "richmenu-f6ce6b077ffd608b59845bbf2fabd3be",
    "LIFF_BUS": "line://app/1586634703-dLEbzgxb",
    "LIFF_BIKE": "line://app/1586634703-MqWqnV6q",
    "LIFF_GMAP": "line://app/1586634703-krVJolxJ",
    "VIDEO_IMAGE": "https://i.imgur.com/KA7yZnl.png",
    "LOCATION_MENU": "https://i.imgur.com/iEHFhIg.png",
    "LOCATION_ICON": "https://i.imgur.com/ZZLbNkM.png"
}
locals().update(GLOBAL)

# ## self lib ###
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "model")))
# from model.apiPtx import apiPtx
# from model.processJson import processJson
# from model.common import common
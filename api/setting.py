# coding: utf-8

### lib ###
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
## file info ##
FileRoute='%s/' %os.path.dirname(os.path.abspath(__file__))
## line info ##
LINE_TOKEN = 'HjFTbjNQhTxrxsvzZHmDewjMd4X26FLt+6ZzMV+wQfzX00KtXBkYN2WnrQ7mZYLhgobRZVLgTryMxaEYgn14sgqOKat6Cz2lT4VFEGC45Z3DGg2/HuckIpAuGWwIhQtV0mUjZ6I7pZo/iJW4noCkqwdB04t89/1O/w1cDnyilFU='
LINE_SECRET = 'eff38d2e8d566ba494f30926d5fdfada'
## MOTC info ##
APPID = 'ad64f3b34d38425ca0bb7efdcdb4548b'
APPKey = 'wabKRdVqcFg4i5CqLXP4JuWQ3Ws'
## google info ##
GOOGLE_MAP_KEY = 'AIzaSyCUx_og-8aUvdj5jDYyQGALwnzlQw_jXok'
## image url ##
IMAGE_URL = "https://worldcrater.com/Ahfargo_bus_bot_free_image"
## richmenu ##
RICH_FUNC = "richmenu-706942f5aa683bff64cc92c491feba79"
RICH_INFO = "richmenu-53795654fb989474b7ae708b44f8a4b6"

## self lib ###
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")))
from motc import motc
from common import common

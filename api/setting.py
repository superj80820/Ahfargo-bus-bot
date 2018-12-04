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
LINE_TOKEN = 'vZwZvgmlljz+VfSYn6Khu2RXQM8Gq3gkODZD8tdHEYgcxsUCI3rHSgh3CO3d7xmXvZ8irnEBQxm1Wughpaj+u1qANpzBavf3VTczraBo+VE4n4QaQpuhGwro/4wMXS1Zde+CyZ0d2Bxk55ZQG4MZBAdB04t89/1O/w1cDnyilFU='
LINE_SECRET = 'c56fe3888c3cfe60a1969fdd19c9b10c'
## MOTC info ##
APPID = 'ad64f3b34d38425ca0bb7efdcdb4548b'
APPKey = 'wabKRdVqcFg4i5CqLXP4JuWQ3Ws'
## google info ##
GOOGLE_MAP_KEY = 'AIzaSyCUx_og-8aUvdj5jDYyQGALwnzlQw_jXok'
## image url ##
IMAGE_URL = "https://worldcrater.com/Ahfargo_bus_bot_image/"
## richmenu ##
RICH_FUNC = "richmenu-ce2919554f6ff106c075bef379923fab"
RICH_INFO = "richmenu-f6ce6b077ffd608b59845bbf2fabd3be"
## liff ##
LIFF_BUS = "line://app/1586634703-dLEbzgxb"
LIFF_BIKE = "line://app/1586634703-MqWqnV6q"
LIFF_GMAP = "line://app/1586634703-krVJolxJ"

## self lib ###
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")))
from motc import motc
from common import common

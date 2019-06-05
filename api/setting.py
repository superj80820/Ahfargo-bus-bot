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
FileRoute = '%s/' %os.path.dirname(os.path.abspath(__file__))
## line info ##
LINE_TOKEN = os.getenv('LINE_TOKEN')
LINE_SECRET = os.getenv('LINE_SECRET')
## MOTC info ##
APPID = os.getenv('MOTC_APPID')
APPKey = os.getenv('MOTC_APPKey')
## google info ##
GOOGLE_MAP_KEY = os.getenv('GOOGLE_MAP_KEY')
## image url ##
IMAGE_URL = os.getenv('IMAGE_URL')
## richmenu ##
RICH_FUNC = os.getenv('RICH_FUNC')
RICH_INFO = os.getenv('RICH_INFO')
## liff ##
LIFF_BUS = os.getenv('LIFF_BUS')
LIFF_BIKE = os.getenv('LIFF_BIKE')
LIFF_GMAP = os.getenv('LIFF_GMAP')

## self lib ###
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")))
from motc import motc
from common import common

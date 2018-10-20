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
import configparser as ConfigParser
from math import sin, cos, sqrt, atan2, radians
from flask import Flask, request, abort, jsonify
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,ImagemapSendMessage,BaseSize,URIImagemapAction,
    ImagemapArea,MessageImagemapAction,FollowEvent,LocationMessage,LocationSendMessage,CarouselTemplate,
    CarouselColumn,PostbackAction,URIAction,MessageAction,TemplateSendMessage
)

## information ##
## file info ##
FileRout=os.path.dirname(os.path.abspath(__file__))+'/'
## line info ##
line_token = 'HjFTbjNQhTxrxsvzZHmDewjMd4X26FLt+6ZzMV+wQfzX00KtXBkYN2WnrQ7mZYLhgobRZVLgTryMxaEYgn14sgqOKat6Cz2lT4VFEGC45Z3DGg2/HuckIpAuGWwIhQtV0mUjZ6I7pZo/iJW4noCkqwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(line_token)
handler = WebhookHandler('eff38d2e8d566ba494f30926d5fdfada')
## MOTC info ##
APPID = 'ad64f3b34d38425ca0bb7efdcdb4548b'
APPKey = 'wabKRdVqcFg4i5CqLXP4JuWQ3Ws'

## self lib ###
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib")))
from motc import motc
from common import common

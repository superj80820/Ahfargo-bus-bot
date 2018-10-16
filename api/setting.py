# coding: utf-8
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

FileRout='/var/www/Ahfargo_bus_bot/api/'
#/var/www/Ahfargo_bus_bot/api/

#line資訊
line_bot_api = LineBotApi('vZwZvgmlljz+VfSYn6Khu2RXQM8Gq3gkODZD8tdHEYgcxsUCI3rHSgh3CO3d7xmXvZ8irnEBQxm1Wughpaj+u1qANpzBavf3VTczraBo+VE4n4QaQpuhGwro/4wMXS1Zde+CyZ0d2Bxk55ZQG4MZBAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('c56fe3888c3cfe60a1969fdd19c9b10c')
#line資訊

#MOTC資訊
APPID = 'ad64f3b34d38425ca0bb7efdcdb4548b'
APPKey = 'wabKRdVqcFg4i5CqLXP4JuWQ3Ws'
#MOTC資訊

sys.path.append('/var/www/Ahfargo_bus_bot/api/lib')
from motc import motc
from common import common

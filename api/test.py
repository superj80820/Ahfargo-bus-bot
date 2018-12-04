from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,ImagemapSendMessage,BaseSize,URIImagemapAction,
    ImagemapArea,MessageImagemapAction,FollowEvent,LocationMessage,LocationSendMessage,CarouselTemplate,
    CarouselColumn,PostbackAction,URIAction,MessageAction,TemplateSendMessage, PostbackEvent
)
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)))))
from setting import *
line_bot_api = LineBotApi(LINE_TOKEN)
handler = WebhookHandler(LINE_SECRET)

def get_word( select, word=None):
    with open("{}res/get_word.json".format(FileRoute), encoding="utf-8") as f:
        json_data = json.load(f)
    if select == 'default':
        for item in json_data[select]:
            for item2 in item['schema']:
                if word.find(item2) != -1: return item['word']
        return None
    else:
        return json_data[select][random.randint(0,len(json_data[select])-1)]

print(get_word("default",'大大'))
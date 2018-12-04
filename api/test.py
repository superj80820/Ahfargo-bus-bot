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

headers = {
    'authorization': 'Bearer HjFTbjNQhTxrxsvzZHmDewjMd4X26FLt+6ZzMV+wQfzX00KtXBkYN2WnrQ7mZYLhgobRZVLgTryMxaEYgn14sgqOKat6Cz2lT4VFEGC45Z3DGg2/HuckIpAuGWwIhQtV0mUjZ6I7pZo/iJW4noCkqwdB04t89/1O/w1cDnyilFU=',
    'content-type': 'application/json'
}
aaa = 

for item in aaa['richmenus']:
    requests.delete("https://api.line.me/v2/bot/richmenu/%s" %(item['richMenuId']),headers=headers)
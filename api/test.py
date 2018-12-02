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

default = '{"events":[{"type":"message","replyToken":"baaa7152be2844eba3e0c0818b16d041","source":{"userId":"Ua594bce22e4cef7b0a70ecfaeb9c5d64","type":"user"},"timestamp":1543721689653,"message":{"type":"text","id":"8945578181047","text":"50"}}],"destination":"U45f9444f8782bce2940871dd8cd05fd6"}'
# groupjoin = {"events":[{"type":"join","replyToken":"581d95a86bb54c42bc3168e6da6e5a04","source":{"groupId":"Cd268da081d4ff17c62e229cecdd50cd1","type":"group"},"timestamp":1543721792017}],"destination":"U45f9444f8782bce2940871dd8cd05fd6"}
# group = {"events":[{"type":"message","replyToken":"999edfd4d6504fbcb854f56deb9828d1","source":{"groupId":"Cd268da081d4ff17c62e229cecdd50cd1","userId":"Ua594bce22e4cef7b0a70ecfaeb9c5d64","type":"group"},"timestamp":1543721822196,"message":{"type":"text","id":"8945586122480","text":"50"}}],"destination":"U45f9444f8782bce2940871dd8cd05fd6"}
# roomjoin = {"events":[{"type":"join","replyToken":"f45c69c426ec4075ae24b8beb3127d52","source":{"roomId":"Rf191c43af61e5db878d40af67cb19785","type":"room"},"timestamp":1543721865589}],"destination":"U45f9444f8782bce2940871dd8cd05fd6"}
# room = {"events":[{"type":"message","replyToken":"d1acccdc7ea14df7a34fd908ad48726f","source":{"roomId":"Rf191c43af61e5db878d40af67cb19785","userId":"Ua594bce22e4cef7b0a70ecfaeb9c5d64","type":"room"},"timestamp":1543721872955,"message":{"type":"text","id":"8945589152766","text":"50"}}],"destination":"U45f9444f8782bce2940871dd8cd05fd6"}

# for item in [default,groupjoin,group,roomjoin,room]:
#     common().user_log(item)

# print(type(ast.literal_eval(default)))
a = lambda d:d if isinstance(d, (list, tuple, dict)) else ast.literal_eval(d)
print(type(default if isinstance(default, (list, tuple, dict)) else ast.literal_eval(default)))
print('yes' if isinstance(default, (list, tuple, dict)) else 'no')
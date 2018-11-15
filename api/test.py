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

common().get_and_save_google_map_image("CmRaAAAAX2odM9LtvPibVIRQJX1Z3NaVAUyQspofwCPJj6qOvdGIOvVVlKShpW714X09wn7pVv3HgU6zOQPhNOmRaxgxhQkwtw4yLmgGLeD6bdG6sqSXDmG9y5RdK6LC50gGPL6xEhA0T2Vfv41qh0LcrRJTuFOSGhQcEIVd6jpIlpXDQCLhwcusLIl8kw")
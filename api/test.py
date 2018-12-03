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

{
  "type": "imagemap",
  "baseUrl": "https://example.com/bot/images/rm001",
  "altText": "This is an imagemap",
  "baseSize": {
      "width": 1040,
      "height": 1040
  },
  "video": {
      "originalContentUrl": "https://example.com/video.mp4",
      "previewImageUrl": "https://example.com/video_preview.jpg",
      "area": {
          "x": 0,
          "y": 0,
          "width": 1040,
          "height": 585
      },
      "externalLink": {
          "linkUri": "https://example.com/see_more.html",
          "label": "See More"
      }
  },
  "actions": [
      {
          "type": "uri",
          "linkUri": "https://example.com/",
          "area": {
              "x": 0,
              "y": 586,
              "width": 520,
              "height": 454
          }
      },
      {
          "type": "message",
          "text": "Hello",
          "area": {
              "x": 520,
              "y": 586,
              "width": 520,
              "height": 454
          }
      }
  ]
}
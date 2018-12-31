
# coding: utf-8
#最後目的地要修改
#附近周遭站牌的檔案限制為10kb 必須要留意 目前已站牌只顯示25個為解決方法 但是因該要採用10kb來限制的方法 才合理
from flask import Flask, request, abort, jsonify
import re
import json
import requests
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
from controller.lineContent import lineContent
from core.route import route
from controller.google import google
from controller.bus import bus as busController
from controller.bike import bike as bikeController
from model.processJson import processJson
from model.common import common
from model.validation import validation

line_bot_api = LineBotApi(LINE_TOKEN)
handler = WebhookHandler(LINE_SECRET)
app = Flask(__name__)
CORS(app)

route = route(LINE_TOKEN)
google = google(GOOGLE_MAP_KEY, FILE_ROUTE)
processJson = processJson(file_route=FILE_ROUTE, global_query=GLOBAL)
common = common()
lineContent = lineContent(google_map_key=GOOGLE_MAP_KEY, file_route=FILE_ROUTE, app_id=APP_ID, app_key=APP_KEY)
validation = validation(file_route=FILE_ROUTE, global_query=GLOBAL)
busController = busController(file_route=FILE_ROUTE, global_query=GLOBAL, app_id=APP_ID, app_key=APP_KEY)
bikeController = bikeController(app_id=APP_ID, app_key=APP_KEY)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # common().user_log(body if isinstance(body, (list, tuple, dict)) else ast.literal_eval(body))
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):
    req = {}
    route\
    .use(lineContent.textWelcome)\
    .use(lineContent.ImagemapWelcome)\
    .use(lineContent.getMessages)\
    .lineReply(event.reply_token, **req)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text=='使用說明':
        req = {}
        route\
        .use(lineContent.textWelcome)\
        .use(lineContent.ImagemapWelcome)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif event.message.text[0:5]=='站牌查詢/':
        req = {"stop_name": event.message.text[5:]}
        route\
        .use(lineContent.flexSearchBusStop)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif re.search('附近站牌\/\d+.\d+,\d+.\d+\/',event.message.text) != None:
        req = {"location": re.search('\d+.\d+,\d+.\d+', event.message.text).group()}
        route\
        .use(lineContent.flexNearbyBusStop)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif re.search('公共自行車\/\d+.\d+,\d+.\d+\/',event.message.text) != None:
        req = {"location": re.search('\d+.\d+,\d+.\d+', event.message.text).group()}
        route\
        .use(lineContent.flexNearbyBike)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif re.search('路線規劃/\d+.\d+,\d+.\d+/',event.message.text) != None:
        req = {"ori_pos": re.search('\d+.\d+,\d+.\d+',event.message.text).group(),"ori_user_id": event.source.user_id}
        route\
        .use(lineContent.flexSetBusRouteConfirm)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif re.search('好玩的/\d+.\d+,\d+.\d+/',event.message.text) != None:
        req = {"location": re.search('\d+.\d+,\d+.\d+', event.message.text).group()}
        route\
        .use(google.getAndSaveGoogleMapImage)\
        .use(lineContent.flexNearbyPlace)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)
    elif event.message.text=='返回選單':
        headers = {'Authorization':'Bearer %s'%(LINE_TOKEN)}
        res=requests.post("https://api.line.me/v2/bot/user/%s/richmenu/%s" %(event.source.user_id, RICH_FUNC),headers=headers)
    elif event.message.text=='更多資訊':
        headers = {'Authorization':'Bearer %s'%(LINE_TOKEN)}
        res=requests.post("https://api.line.me/v2/bot/user/%s/richmenu/%s" %(event.source.user_id, RICH_INFO),headers=headers)
    else:
        req = {"word": event.message.text, "city": "Taichung"}
        route\
        .use(validation.checkLineUserMessage)\
        .use(lineContent.textGetWord)\
        .use(lineContent.flexBusInfo)\
        .use(lineContent.getMessages)\
        .lineReply(event.reply_token, **req)

    lineContent.clearMessages()

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    if validation.checkLocation(event, ["台中", "臺中"]):
        check = validation.checkUserRouteActionAgain(event.source.user_id)
        if check == "in set":
            req = {"destination": '%s,%s'%(event.message.latitude,event.message.longitude), "city": "Taichung", "user_id": event.source.user_id}
            route\
            .use(lineContent.flexSetBusRoute)\
            .use(lineContent.getMessages)\
            .lineReply(event.reply_token, **req)
        elif check == "in beging":
            req = {"line_event": event}
            route\
            .use(lineContent.ImagemapLocationMenu)\
            .use(lineContent.getMessages)\
            .lineReply(event.reply_token, **req)
    else:
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='這個區域目前不支援呱\n台中市以外的其他縣市火速開發中!'))

    lineContent.clearMessages()

@app.route('/bus', methods=['GET'])
def bus():
    req = dict(request.args)
    return route\
    .use(busController.stopPos)\
    .use(busController.busPos)\
    .reply(**req)

@app.route('/bus_path', methods=['GET'])
def bus_path():
    req = dict(request.args)
    return route\
    .use(busController.busPath)\
    .reply(**req)

@app.route('/bus_all_num', methods=['GET'])
def bus_all_num():
    req = dict(request.args)
    return route\
    .use(busController.busAllNum)\
    .reply(**req)

@app.route('/bike', methods=['GET'])
def bike():
    req = dict(request.args)
    return route\
    .use(bikeController.realTime)\
    .reply(**req)

if __name__ == "__main__":
    app.run(debug=True)

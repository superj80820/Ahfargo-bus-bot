
# coding: utf-8
#最後目的地要修改
#附近周遭站牌的檔案限制為10kb 必須要留意 目前已站牌只顯示25個為解決方法 但是因該要採用10kb來限制的方法 才合理
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
app = Flask(__name__)
CORS(app)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    print(body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(FollowEvent)
def handle_follow(event):
    imagemap_message = ImagemapSendMessage(
            base_url='https://i.imgur.com/KFPyBnS.jpg',
            alt_text='this is an imagemap',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://example.com/',
                    area=ImagemapArea(
                        x=0, y=0, width=520, height=1040
                    )
                ),
                MessageImagemapAction(
                    text='hello',
                    area=ImagemapArea(
                        x=520, y=0, width=520, height=1040
                    )
                )
            ]
        )
    line_bot_api.reply_message(
        event.reply_token, imagemap_message)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        int(event.message.text)
        sent_is_what=True
    except ValueError as e1:
        sent_is_what=False
    
    if sent_is_what==True:
        bus_id=event.message.text
        print(bus_id)

        headers=common().RES_HEAD(APPID,APPKey)

        res=requests.get('http://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taichung/'+bus_id+'?$format=JSON',headers=headers)
        json_data=json.loads(res.text)
        #print(json_data)
        res_pos=requests.get('http://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/City/Taichung/'+bus_id+'?$format=JSON',headers=headers)
        json_data_pos=json.loads(res_pos.text)
        #print(json_data_pos)

        sent_dict1=[]
        sent_dict2=[]
        sent_ans1=''
        sent_ans2=''
        format = '%Y-%m-%dT%H:%M:%S+08:00'
        localtime=time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime())

        for item in json_data:
            if item['Direction']==0 and str(item['RouteID'])==bus_id:
                try:
                    #NextBusTime=datetime.datetime.strptime(item['NextBusTime'], format)-datetime.datetime.strptime(localtime, format)
                    #NextBusTime=str(NextBusTime)
                    if item['EstimateTime']>180:
                        EstimateTime=item['EstimateTime']/60
                    elif item['EstimateTime']>=0:
                        EstimateTime='即將進站'
                    elif item['EstimateTime']==-3:
                        EstimateTime='離駛'
                    else:
                        EstimateTime='未發'
                    sent_dict1+=[{'sent_name1':item['StopName']['Zh_tw'],'sent_id1':item['StopSequence'],'sent_time1':EstimateTime}]
                except KeyError as e1:
                    sent_dict1+=[{'sent_name1':item['StopName']['Zh_tw'],'sent_id1':item['StopSequence'],'sent_time1':'尚未發車'}]
            if item['Direction']==1 and str(item['RouteID'])==bus_id:
                try:
                    #NextBusTime=datetime.datetime.strptime(item['NextBusTime'], format)-datetime.datetime.strptime(localtime, format)
                    #NextBusTime=str(NextBusTime)
                    if item['EstimateTime']>180:
                        EstimateTime=item['EstimateTime']/60
                    elif item['EstimateTime']>=0:
                        EstimateTime='即將進站'
                    elif item['EstimateTime']==-3:
                        EstimateTime='離駛'
                    else:
                        EstimateTime='未發'
                    sent_dict2+=[{'sent_name2':item['StopName']['Zh_tw'],'sent_id2':item['StopSequence'],'sent_time2':EstimateTime}]
                except KeyError as e1:
                    sent_dict2+=[{'sent_name2':item['StopName']['Zh_tw'],'sent_id2':item['StopSequence'],'sent_time2':'尚未發車'}]

        sent_dict1.sort(key=lambda d:d['sent_id1']) 
        sent_dict2.sort(key=lambda d:d['sent_id2'])  

        for item in sent_dict1:
            sent_ans1+=str(item['sent_id1'])+'.'+item['sent_name1']+' '+str(item['sent_time1'])+'\n'
        for item in sent_dict2:
            sent_ans2+=str(item['sent_id2'])+'.'+item['sent_name2']+' '+str(item['sent_time2'])+'\n'
        sent_ans1=sent_ans1[0:len(sent_ans1)-1]
        sent_ans2=sent_ans2[0:len(sent_ans2)-1]    
        
        if sent_dict1==[] or sent_dict2==[]:
            line_bot_api.reply_message(
                event.reply_token,[TextSendMessage(text='沒有這台公車呱')])
        else:
            line_bot_api.reply_message(
                event.reply_token,[TextSendMessage(text='往'+sent_dict1[len(sent_dict1)-1]['sent_name1']+'：\n'+sent_ans1),
                                   TextSendMessage(text='往'+sent_dict2[len(sent_dict2)-1]['sent_name2']+'：\n'+sent_ans2)])
                                   #刪除PM2.5功能TextSendMessage(text=DUST2_5_IS_WHAT(json_data_pos))
            
    elif event.message.text=='使用方法':
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='請直接輸入公車號即可查詢呱!'))
    
    elif event.message.text=='公車查詢':
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='圖表正在製作中 呱呱!'))

    elif re.search('附近站牌/\d+.\d+,\d+.\d+/',event.message.text) != None:
        location_temp = re.search('\d+.\d+,\d+.\d+',event.message.text).group()
        location_temp_list = location_temp.split(',')
        location = {}
        location['lat'] = float(location_temp_list[0])
        location['lon'] = float(location_temp_list[1])
        flex = common().creat_stop_contents(location, 0.5)
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif re.search('路線規劃/\d+.\d+,\d+.\d+/',event.message.text) != None:
        flex={
            "type":"flex",
            "altText":"This is a Flex Message",
            "contents":{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.clipartlogo.com/files/istock/previews/8976/89765575-duck-icon-farm-animal-vector-illustration.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "你附近的公車站～嘎",
                            "weight": "bold",
                            "size": "xl"
                            }
                        ]
                    },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "xs",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "gravity": "center",
                                "action": {
                                    "type": "uri",
                                    "label": "請選擇目的地~呱",
                                    "uri": "line://nv/location"
                                },
                                "flex": 1
                                }
                            ]
                        }
                    ],
                    "flex": 0
                }
            }
        }
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif re.search('好玩的/\d+.\d+,\d+.\d+/',event.message.text) != None:
        flex={
            "type":"flex",
            "altText":"This is a Flex Message",
            "contents":{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://images.clipartlogo.com/files/istock/previews/8976/89765575-duck-icon-farm-animal-vector-illustration.jpg",
                    "size": "full",
                    "aspectRatio": "20:13",
                    "aspectMode": "cover",
                    "action": {
                    "type": "uri",
                    "uri": "http://linecorp.com/"
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "你想去哪玩~呱",
                            "weight": "bold",
                            "size": "xl"
                            }
                        ]
                    },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "xs",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "gravity": "center",
                                "action": {
                                    "type": "uri",
                                    "label": "找景點/12334G23GR42G233",
                                    "uri": "line://nv/location"
                                },
                                "flex": 1
                                },
                                {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "gravity": "center",
                                "action": {
                                    "type": "uri",
                                    "label": "玩活動/12334G23GR42G233",
                                    "uri": "line://nv/location"
                                },
                                "flex": 1
                                }
                            ]
                        }
                    ],
                    "flex": 0
                }
            }
        }
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif event.message.text=='test':
        location = {}
        location['lat'] = float(24.138777)
        location['lon'] = float(120.671274)
        flex = common().creat_stop_contents(location, 0.5)
        
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[{
                    "type": "location",
                    "title": "my location",
                    "address": "〒150-0002 東京都渋谷区渋谷２丁目２１−１",
                    "latitude": 35.65910807942215,
                    "longitude": 139.70372892916203
                }]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

@handler.add(PostbackEvent)
def handle_postback(event):
    # if event.postback.data == 'plan':
    #     imagemap = {
    #         "type": "imagemap",
    #         "baseUrl": "https://i.imgur.com/43SaaBB.png",
    #         "altText": "This is an imagemap",
    #         "baseSize": {
    #             "width": 1040,
    #             "height": 310
    #         },
    #         "actions": [
    #             {
    #             "type": "message",
    #             "area": {
    #                 "x": 0,
    #                 "y": 0,
    #                 "width": 338,
    #                 "height": 309
    #             },
    #             "text": "動作 1"
    #             },
    #             {
    #             "type": "message",
    #             "area": {
    #                 "x": 338,
    #                 "y": 1,
    #                 "width": 347,
    #                 "height": 309
    #             },
    #             "text": "動作 2"
    #             },
    #             {
    #             "type": "message",
    #             "area": {
    #                 "x": 685,
    #                 "y": 1,
    #                 "width": 355,
    #                 "height": 309
    #             },
    #             "text": "動作 3"
    #             }
    #         ]
    #         }
    #     headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
    #     payload = {
    #         'replyToken':event.reply_token,
    #         'messages':[flex]
    #         }
    #     res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
    #     print(res.text)
    # elif event.postback.data == 'route_plan':
    #     line_bot_api.reply_message(
    #         event.reply_token, TextSendMessage(text='pong'))
    None

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    print(str(float(event.message.latitude)))
    print(str(float(event.message.longitude)))
    imagemap = {
        "type": "imagemap",
        "baseUrl": "https://i.imgur.com/7HFxSMt.png",
        "altText": "This is an imagemap",
        "baseSize": {
            "width": 1040,
            "height": 310
        },
        "actions": [
            {
            "type": "message",
            "area": {
                "x": 0,
                "y": 0,
                "width": 255,
                "height": 309
            },
            "text": "附近站牌/%s,%s/" %(str(event.message.latitude), str(event.message.longitude))
            },
            {
            "type": "message",
            "area": {
                "x": 255,
                "y": 1,
                "width": 263,
                "height": 309
            },
            "text": "路線規劃/%s,%s/" %(str(event.message.latitude), str(event.message.longitude))
            },
            {  
            "type":"uri",
            "label":"公共自行車/%s,%s/" %(str(event.message.latitude), str(event.message.longitude)),
            "linkUri":"line://app/1615663243-36r5Y25z?pos=%sand%s" %(str(event.message.latitude), str(event.message.longitude)),
            "area":{  
                "x": 518,
                "y": 1,
                "width": 255,
                "height": 309
                }
            },
            {
            "type": "message",
            "area": {
                "x": 773,
                "y": 0,
                "width": 267,
                "height": 310
            },
            "text": "好玩的/%s,%s/" %(str(event.message.latitude), str(event.message.longitude))
            }
        ]
        }
    headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
    payload = {
        'replyToken':event.reply_token,
        'messages':[imagemap]
        }
    res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
    # res=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=景點&location=%s&radius=500&key=AIzaSyD9ojwRyJKMDqorLnjpoaRT7s94S2EAkVA&language=zh-TW'%loc)
    # sent_data=json.loads(res.text)
    # columns=[]

    # count=0
    # for item in sent_data['results']:
    #     if count==10:
    #         break
    #     columns+=[CarouselColumn(text=item['vicinity'], title=item['name'], actions=[
    #         URIAction(label='搜尋看看!', uri='https://www.google.com.tw/maps/search/%s'%item['name']),
    #         MessageAction(label='我喜歡這裡呱!', text='%s我覺得不錯'%item['name'])])]
    #     count+=1
        
    # carousel_template = CarouselTemplate(columns=columns)
    # template_message = TemplateSendMessage(
    #     alt_text='Carousel alt text', template=carousel_template)
    
    # line_bot_api.reply_message(event.reply_token, template_message)

@app.route('/bus', methods=['GET'])
def bus():
    RouteName=request.args.get('RouteName')
    Direction=request.args.get('Direction')
    City=request.args.get('City')

    headers=common().RES_HEAD(APPID,APPKey)
    res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/%s?$filter=RouteName/Zh_tw eq '%s' and Direction eq '%s'&$orderby=StopSequence asc&$format=JSON"%(City, RouteName, Direction),headers=headers)
    json_data=json.loads(res.text)
    # print(json_data)

    return jsonify(json_data)
        
@app.route('/bus_path', methods=['GET'])
def bus_path():
    test = "LINESTRING(120.678157999892 24.1932940004178,120.680200999676 24.1929449996121,120.682208999646 24.1923989996142,120.682363999599 24.1921220003301,120.682724000013 24.1919699996158,120.683432000287 24.1915930002168,120.684993000327 24.1905030003132,120.686250999884 24.1887749997665,120.68625700016 24.1864090003751,120.686153999907 24.1822280000222,120.685905000116 24.1782789995762,120.685732000232 24.1749459996582,120.685521000394 24.1720239998078,120.685152999611 24.1684640002135,120.685045000027 24.1654840003864,120.685017999681 24.1630559999345,120.686672000413 24.1630430002343,120.689775999663 24.1629030000735,120.691177999565 24.1629179998658,120.69216099993 24.1625609995905,120.692397000022 24.1622220001452,120.692440000206 24.1617900000085,120.691298999749 24.159070999627,120.686193999953 24.154794000243,120.684318999822 24.150378999891,120.683437999664 24.1483129999451,120.683205999757 24.1476340001091,120.682476000267 24.1458899997237,120.68181300027 24.1446320001667,120.682824000128 24.1436210003089,120.684414999752 24.1422399995764,120.685237999934 24.1430530001958,120.685364000348 24.143177999665,120.685530999956 24.1432290002182,120.685739999701 24.1432189997571,120.685769000139 24.1415569995559,120.685791000255 24.1402820001143,120.685890000323 24.1401130004147,120.685814999563 24.1400500002074,120.685850000277 24.1398510000237,120.685922 24.139793000047,120.684728999844 24.139185999934,120.683226999826 24.1378250001237,120.684364000099 24.1369039999197,120.682232999853 24.1358659997161,120.68296100015 24.1344130001599,120.67658700029 24.1317840003314,120.666546000398 24.1276179997709,120.665577999825 24.1269260002348,120.661695999771 24.1219609997004,120.658766999597 24.1179879999463,120.656022999862 24.1155750001861,120.650928999674 24.112048000315,120.644439999906 24.109730999586,120.636276000237 24.1072779997799,120.631608999955 24.1051359999265,120.628549000036 24.1056349995557,120.624084000077 24.1064060000369,120.618864000373 24.1065559997596,120.616018999577 24.1059669995774,120.614105000346 24.1068699998507,120.609143999996 24.1079419998235,120.601932000162 24.1103759996527,120.591821999786 24.1136359998016,120.587574999986 24.1131390002647,120.585687000155 24.11363899994,120.584398000068 24.1151549997035,120.581596000355 24.1169200001579,120.576633999959 24.1188379995741,120.571554000417 24.1207499996128,120.564552000375 24.1234170002944,120.557898000193 24.1274019997026,120.555404000294 24.1292830001104,120.554515999814 24.1313890001023,120.55372200007 24.1347949997894,120.552313999891 24.1365649995751,120.550235000245 24.1392399997263,120.548092000346 24.1435349999404,120.546529000213 24.1470759995578,120.5459739998 24.1498780001696,120.544447999576 24.1543300004292,120.544065999946 24.1588799998122,120.543121999581 24.1634229997717,120.542516000413 24.1691169997498,120.54362600034 24.1739359998465,120.544502000267 24.177414000156,120.545288999688 24.1807989997741,120.54508300008 24.182914000181,120.545263000287 24.1878769997238,120.545654000332 24.1922370002374,120.546169999846 24.1961499999226,120.546420999729 24.1982099995919,120.547314000441 24.2013060002718,120.548213999676 24.2041710001915,120.548445000436 24.2061339998842,120.550209999992 24.2100240003074,120.551884200396 24.2137588299061)"
    test = test[11:len(test)-1]
    test = test.split(",")
    new_test=[]
    for item in range(0,len(test)):
        for item2 in range(0,len(test[item].split(" "))):
            if item2 == 0:
                lon = float(test[item].split(" ")[item2])
            elif item2 == 1:
                lat = float(test[item].split(" ")[item2])
        new_test += [[lat,lon]]
    print(new_test)
    return jsonify(new_test)

if __name__ == "__main__":
    app.run()

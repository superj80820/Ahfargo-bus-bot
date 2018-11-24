
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
    def sent_user(BusNum):
        flex={
            "type":"flex",
            "altText":"This is a Flex Message",
            "contents":{
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "請點選觀看動態~",
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
                                    "label": "點我~~呱呱",
                                    "uri": "line://app/1615663243-gkN06e02?BusNum=%s&City=%s&Direction=0" %(BusNum, 'Taichung')
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
        return flex

    with open("{}res/route.json".format(FileRoute),'rb') as f:
        data = json.load(f)
    for item in data:
        if event.message.text==item['RouteName']['Zh_tw']:
            flex = sent_user(event.message.text)
            message = {"type": "text","text": common().get_word("bus_num")}
            headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
            payload = {
                'replyToken':event.reply_token,
                'messages':[flex, message]
                }
            res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
            break
            
    if event.message.text=='使用方法':
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='請直接輸入公車號即可查詢呱!'))
    
    elif event.message.text[0:5]=='站牌查詢/':
        headers=common().RES_HEAD(APPID,APPKey)
        res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taichung?$select=RouteName&$filter=Stops/any(d:d/StopName/Zh_tw eq '%s')&$format=JSON"%(event.message.text[5:len(event.message.text)]),headers=headers)
        json_data=json.loads(res.text)
        content = []
        new_content = []
        temp = ''
        for item in json_data:
            content += [item['RouteName']['Zh_tw']]
        content = list(set(content))
        for i in range(0,len(content)-1): #有n-1回合(n為數字個數)
            for j in range(0,len(content)-1-i): #每回合進行比較的範圍
                if int(re.search('\d+',str(content[j])).group()) > int(re.search('\d+',str(content[j+1])).group()):
                    tmp = content[j]
                    content[j] = content[j+1]
                    content[j+1] = tmp
        print(content)
        flex = common().creat_bus_contents(content)
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif re.search('附近站牌/\d+.\d+,\d+.\d+/',event.message.text) != None:
        location_temp = re.search('\d+.\d+,\d+.\d+',event.message.text).group()
        location_temp_list = location_temp.split(',')
        location = {}
        location['lat'] = float(location_temp_list[0])
        location['lon'] = float(location_temp_list[1])
        message = {"type": "text","text": common().get_word("nearby_bus")}
        # print("aaaaaaaa"+message)
        flex = common().creat_stop_contents(location, 0.5)
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex, message]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif re.search('公共自行車/\d+.\d+,\d+.\d+/',event.message.text) != None:
        location_temp = re.search('\d+.\d+,\d+.\d+',event.message.text).group()
        location_temp_list = location_temp.split(',')
        location = {}
        location['lat'] = float(location_temp_list[0])
        location['lon'] = float(location_temp_list[1])
        flex={
            "type":"flex",
            "altText":"This is a Flex Message",
            "contents":{
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "這是你附近的腳踏車喔!",
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
                                    "label": "點這觀看地圖~",
                                    "uri": "line://app/1615663243-36r5Y25z?pos=%sand%s" %(str(location['lat']), str(location['lon']))
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
        message = {"type": "text","text": common().get_word("nearby_bike")}
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex, message]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif re.search('路線規劃/\d+.\d+,\d+.\d+/',event.message.text) != None:
        ori_pos = re.search('\d+.\d+,\d+.\d+',event.message.text).group()
        conn = sqlite.connect('%sdata/db/user_action.db'%(FileRoute))
        c = conn.cursor()
        user_id = c.execute('SELECT user_id FROM route_plan WHERE user_id ="%s"'%(event.source.user_id))
        user_id = user_id.fetchall()
        print(user_id)
        if user_id != []:
            print('update')
            c.execute('UPDATE route_plan SET planing ="action" WHERE user_id ="%s"'%(event.source.user_id))
            c.execute('UPDATE route_plan SET pos ="%s" WHERE user_id ="%s"'%(ori_pos, event.source.user_id))
        else:
            print('insert')
            c.execute('INSERT INTO route_plan (user_id,planing,pos) VALUES ("%s","action","%s")'%(event.source.user_id, ori_pos))
        conn.commit()
        conn.close()

        flex={
            "type":"flex",
            "altText":"This is a Flex Message",
            "contents":{
                "type": "bubble",
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
        ori_pos = re.search('\d+.\d+,\d+.\d+',event.message.text).group()
        res=requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=景點&location=%s&radius=1000&key=AIzaSyD9ojwRyJKMDqorLnjpoaRT7s94S2EAkVA&language=zh-TW'%ori_pos)
        sent_data=json.loads(res.text)
        message = {"type": "text","text": common().get_word("fun_place")}
        print(sent_data)
        columns=[]
        if sent_data['status'] != 'ZERO_RESULTS':
            flex = common().nearby_place(sent_data, ori_pos)
            headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
            payload = {
                'replyToken':event.reply_token,
                'messages':[flex, message]
                }
            res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
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
        else:
            line_bot_api.reply_message(
                event.reply_token,TextSendMessage(text='目前我不太知道附近有甚麼好玩的...呱呱'))
        # flex={
        #     "type":"flex",
        #     "altText":"This is a Flex Message",
        #     "contents":{
        #         "type": "bubble",
        #         "hero": {
        #             "type": "image",
        #             "url": "https://images.clipartlogo.com/files/istock/previews/8976/89765575-duck-icon-farm-animal-vector-illustration.jpg",
        #             "size": "full",
        #             "aspectRatio": "20:13",
        #             "aspectMode": "cover",
        #             "action": {
        #             "type": "uri",
        #             "uri": "http://linecorp.com/"
        #             }
        #         },
        #         "body": {
        #             "type": "box",
        #             "layout": "vertical",
        #             "contents": [
        #                 {
        #                     "type": "text",
        #                     "text": "你想去哪玩~呱",
        #                     "weight": "bold",
        #                     "size": "xl"
        #                     }
        #                 ]
        #             },
        #         "footer": {
        #             "type": "box",
        #             "layout": "vertical",
        #             "spacing": "xs",
        #             "contents": [
        #                 {
        #                     "type": "box",
        #                     "layout": "horizontal",
        #                     "contents": [
        #                         {
        #                         "type": "button",
        #                         "style": "link",
        #                         "height": "sm",
        #                         "gravity": "center",
        #                         "action": {
        #                             "type": "uri",
        #                             "label": "找景點/12334G23GR42G233",
        #                             "uri": "line://nv/location"
        #                         },
        #                         "flex": 1
        #                         },
        #                         {
        #                         "type": "button",
        #                         "style": "link",
        #                         "height": "sm",
        #                         "gravity": "center",
        #                         "action": {
        #                             "type": "uri",
        #                             "label": "玩活動/12334G23GR42G233",
        #                             "uri": "line://nv/location"
        #                         },
        #                         "flex": 1
        #                         }
        #                     ]
        #                 }
        #             ],
        #             "flex": 0
        #         }
        #     }
        # }
        # headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        # payload = {
        #     'replyToken':event.reply_token,
        #     'messages':[flex]
        #     }
        # res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

    elif event.message.text=='test':
        conn = sqlite.connect('%sdata/db/user_action.db'%(FileRoute))
        c = conn.cursor()
        user_id = c.execute('SELECT user_id FROM route_plan WHERE user_id ="%s"'%(event.source.user_id))
        user_id = user_id.fetchall()
        print(user_id)
        if user_id != []:
            print('update')
            c.execute('UPDATE route_plan SET planing ="action" WHERE user_id ="%s"'%(event.source.user_id))
        else:
            print('insert')
            c.execute('INSERT INTO route_plan (user_id,planing) VALUES ("%s","action")'%(event.source.user_id))
        conn.commit()
        conn.close()
            

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
    conn = sqlite.connect('%sdata/db/user_action.db'%(FileRoute))
    c = conn.cursor()
    planing = c.execute('SELECT planing FROM route_plan WHERE user_id ="%s"'%(event.source.user_id))
    planing = planing.fetchall()
    print(planing)
    if planing == [('action',)]:
        print('in origin')
        ori_pos = c.execute('SELECT pos FROM route_plan WHERE user_id ="%s"'%(event.source.user_id))
        ori_pos = ori_pos.fetchall()
        print(ori_pos[0][0])
        c.execute('DELETE FROM route_plan WHERE user_id ="%s"'%(event.source.user_id))
        flex = common().set_bus_route(ori_pos[0][0], str(float(event.message.latitude))+','+str(float(event.message.longitude)))
        message = {"type": "text","text": common().get_word("route_plan")}
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex, message]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
        print(res.text)
    elif planing == []:
        print('in begin')
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
                "type": "message",
                "area": {
                    "x": 518,
                    "y": 1,
                    "width": 255,
                    "height": 309
                },
                "text": "公共自行車/%s,%s/" %(str(event.message.latitude), str(event.message.longitude))
                }
                ,
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
        
    conn.commit()
    conn.close()

@app.route('/bus', methods=['GET'])
def bus():
    def get_bus_pos(json_data,start,end):
        headers=common().RES_HEAD(APPID,APPKey)
        res_pos_filter="StopUID eq"
        for item in range(start,end):
            res_pos_filter += " '%s' or StopUID eq"%(json_data[item]['StopUID'])
        res_pos_filter = res_pos_filter[0:len(res_pos_filter)-14]
        res_pos=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$filter=%s&$format=JSON"%(res_pos_filter),headers=headers)
        json_data_pos=json.loads(res_pos.text)
        return json_data_pos

    def get_all_bus(Direction, City, RouteName):
        headers=common().RES_HEAD(APPID,APPKey)
        res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/%s?$filter=RouteName/Zh_tw eq '%s' and Direction eq '%s'&$orderby=StopSequence asc&$format=JSON"%(City, RouteName, Direction),headers=headers)
        json_data=json.loads(res.text)
        # print(json_data)

        # 避免一次請求參數太常造成問題
        count_half=int(len(json_data)/2)
        json_data_pos_all = []
        json_data_pos_all += get_bus_pos(json_data,0,count_half)
        json_data_pos_all += get_bus_pos(json_data,count_half,len(json_data))
        # 避免一次請求參數太常造成問題
        
        for item in json_data_pos_all:
            for item2 in range(0,len(json_data)):
                if item['StopUID'] == json_data[item2]['StopUID']:
                    json_data[item2]['StopPosition']=item['StopPosition']
        # print(json_data)
        return json_data
    
    def get_bus_star_and_end(RouteName):
        headers=common().RES_HEAD(APPID,APPKey)
        res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?$select=DepartureStopNameZh,DestinationStopNameZh&$filter=RouteName/Zh_tw eq '%s'&$format=JSON"%(RouteName),headers=headers)
        json_data=json.loads(res.text)
        return json_data

    def get_bus_lat_lon(index,ret):
        bus_pos=[]
        sent_numb = "PlateNumb eq"
        for item in ret[index]:
            if item.get('PlateNumb') and item['PlateNumb'] != '' and item['PlateNumb'] not in bus_pos:
                bus_pos += [item['PlateNumb']]
                sent_numb += " '%s' or PlateNumb eq"%item['PlateNumb']
        sent_numb = sent_numb[0:len(sent_numb)-16]
        headers=common().RES_HEAD(APPID,APPKey)
        res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/City/Taichung?$filter=%s&$format=JSON"%(sent_numb),headers=headers)
        json_data=json.loads(res.text)
        for item in json_data:
            for item2 in ret[index]:
                if item2.get('PlateNumb') and item2['PlateNumb'] == item['PlateNumb']:
                    item2['BusPosition'] = item['BusPosition']
        return ret

    RouteName=request.args.get('RouteName')
    City=request.args.get('City')

    ret=[]
    ret += [get_all_bus('0', City, RouteName)]
    ret += [get_all_bus('1', City, RouteName)]
    ret += [get_bus_star_and_end(RouteName)]
    
    ret = get_bus_lat_lon(0,ret)
    ret = get_bus_lat_lon(1,ret)

    return jsonify(ret)
        
@app.route('/bus_path', methods=['GET'])
def bus_path():
    def pathM(path_data):
        point = []
        ans = []
        final_ans = []
        temp = []
        count = 0
        path_data = path_data[1:len(path_data)-1]
        for item in path_data:
            if item == '(':
                point+=[count]
            if item == ')':
                for item2 in path_data[point[len(point)-1]+1:count].split(','):
                    temp_1,temp_2 = item2.split(' ')
                    temp += [[float(temp_2),float(temp_1)]]
                ans += [temp]
                temp = []
                point.pop()
            count += 1
        for item in range(0,len(ans)):
            if item != len(ans)-1:#check all(except start)
                if abs(ans[item][0][0]-ans[item+1][0][0])>abs(ans[item][0][0]-ans[item+1][len(ans[item+1])-1][0]):
                    print('revert')
                    ans[item+1].reverse()
            else:#check start
                if abs(ans[0][0][0]-ans[1][0][0])<abs(ans[0][len(ans[0])-1][0]-ans[1][0][0]):
                    print('start_revert')
                    ans[0].reverse()
        for item in ans:
            final_ans.extend(item)
        return final_ans

    def pathL(path_data):
        point = []
        ans = []
        final_ans = []
        temp = []
        count = 0
        for item in path_data:
            if item == '(':
                point+=[count]
            if item == ')':
                for item2 in path_data[point[len(point)-1]+1:count].split(','):
                    temp_1,temp_2 = item2.split(' ')
                    temp += [[float(temp_2),float(temp_1)]]
                ans += temp
                temp = []
                point.pop()
            count += 1
        final_ans.extend(ans)
        return final_ans

    bus_name=request.args.get('bus_name')
    headers=common().RES_HEAD(APPID,APPKey)
    res=requests.get("http://ptx.transportdata.tw/MOTC/v2/Bus/Shape/City/Taichung?$filter=RouteName/Zh_tw eq '%s'&$orderby=Direction asc&$format=JSON"%(bus_name),headers=headers)
    json_data=json.loads(res.text)

    ret = {}

    path_data = re.search('[\d,.() ]+',json_data[0]['Geometry']).group()
    if json_data[0]['Geometry'][0] == "L":
        print('inL')
        path_l = pathL(path_data)
        ret['Geometry0'] = path_l
    elif json_data[0]['Geometry'][0] == "M":
        print('inM')
        path_m = pathM(path_data)
        ret['Geometry0'] = path_m

    path_data = re.search('[\d,.() ]+',json_data[1]['Geometry']).group()
    if json_data[1]['Geometry'][0] == "L":
        print('inL')
        path_l = pathL(path_data)
        ret['Geometry1'] = path_l
    elif json_data[1]['Geometry'][0] == "M":
        print('inM')
        path_m = pathM(path_data)
        ret['Geometry1'] = path_m

    return jsonify(ret)

@app.route('/bus_all_num', methods=['GET'])
def bus_all_num():
    headers=common().RES_HEAD(APPID,APPKey)
    res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?$select=RouteName,RouteID,SubRoutes&$format=JSON",headers=headers)
    json_data=json.loads(res.text)
    json_data.sort(key=lambda d:int(d['RouteID']))
    print(json_data)
    return jsonify(json_data)

if __name__ == "__main__":
    app.run()

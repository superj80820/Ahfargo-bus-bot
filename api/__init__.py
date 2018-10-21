
# coding: utf-8
#最後目的地要修改
#附近周遭站牌的檔案限制為10kb 必須要留意 目前已站牌只顯示25個為解決方法 但是因該要採用10kb來限制的方法 才合理
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
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)))))
from setting import *
line_bot_api = LineBotApi(LINE_TOKEN)
handler = WebhookHandler(LINE_SECRET)
app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
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

    elif event.message.text=='test':
        location = {}
        location['lat'] = float(24.138777)
        location['lon'] = float(120.671274)
        flex = common().creat_stop_contents(location, 0.5)
        
        headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
        payload = {
            'replyToken':event.reply_token,
            'messages':[flex]
            }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    print(event.message.title)
    location = {}
    location['lat'] = float(event.message.latitude)
    location['lon'] = float(event.message.longitude)
    flex = common().creat_stop_contents(location, 0.5)
    
    headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(LINE_TOKEN)}
    payload = {
        'replyToken':event.reply_token,
        'messages':[flex]
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
    City=request.args.get('City')
    ret = {}
    ret['Direction1'] = {}
    ret['Direction2'] = {}
    sent_is_what=True

    if sent_is_what==True:
        bus_id=RouteName
        print(bus_id)

        headers=common().RES_HEAD(APPID,APPKey)

        res=requests.get('http://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/%s/%s?$format=JSON'%(City, bus_id),headers=headers)
        json_data=json.loads(res.text)
        #print(json_data)

        sent_dict1=[]
        sent_dict2=[]
        # format = '%Y-%m-%dT%H:%M:%S+08:00'
        # localtime=time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime())

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
                    sent_dict1+=[{'sent_name1':item['StopName']['Zh_tw'],'sent_id1':item['StopSequence'],'sent_time1':EstimateTime,'bus_uid':item['SubRouteUID']}]
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
                    sent_dict2+=[{'sent_name2':item['StopName']['Zh_tw'],'sent_id2':item['StopSequence'],'sent_time2':EstimateTime,'bus_uid':item['SubRouteUID']}]
                except KeyError as e1:
                    sent_dict2+=[{'sent_name2':item['StopName']['Zh_tw'],'sent_id2':item['StopSequence'],'sent_time2':'尚未發車'}]

        sent_dict1.sort(key=lambda d:d['sent_id1']) 
        sent_dict2.sort(key=lambda d:d['sent_id2'])     

        ret['Direction1']['name'] = sent_dict1[len(sent_dict1)-1]['sent_name1']
        ret['Direction2']['name'] = sent_dict2[len(sent_dict2)-1]['sent_name2']
        ret['Direction1']['data'] = sent_dict1
        ret['Direction2']['data'] = sent_dict2

        if sent_dict1==[] or sent_dict2==[]:
            return "No Route"
        else:
            return jsonify(ret)
        
if __name__ == "__main__":
    app.run()


# coding: utf-8

# In[ ]:


#最後目的地要修改
import sys
sys.path.append('/var/www/Ahfargo_bus_bot/api')
from setting import *

#製作驗證簽名
def RES_HEAD(APPID,APPKey):
    X_Date=datetime.datetime.now(datetime.timezone.utc).strftime("%a, "+"%d %b "+"%Y %H:%M:%S"+" GMT")
    print(X_Date)

    sent_APPKey = str.encode(APPKey)
    sent_time = str.encode("x-date: "+X_Date)
    hmac_ans = hmac.new(sent_APPKey,sent_time ,sha1)
    hmac_ans=base64.b64encode(hmac_ans.digest())
    hmac_ans=str(hmac_ans)[2:len(str(hmac_ans))-1]
    print(hmac_ans)

    Authorization='hmac username="'+APPID+'", algorithm="hmac-sha1", headers="x-date", signature="'+hmac_ans+'"'

    headers={ 'Authorization': Authorization, 'X-Date':X_Date}
    return headers
#時間轉min
def GET_SEC(time_str):
    h, m, s = time_str.split(':')
    try:
        sent=int(h) * 60 + int(m) 
    except ValueError as e1:
        sent=time_str
    return sent
def DUST2_5_IS_WHAT(json_data_pos):
    json_data_AQI=''
    res_AQI=requests.get('https://airmap.g0v.asper.tw/json/airmap.json')
    json_data_AQI=json.loads(res_AQI.text)
    scale=100#pm2.5倍率
    dust_data=[]
    map_ori_list=[]
    map_ori=''
    map_des=''
    get_map=[]
    if json_data_pos!=[]:
        posLat=json_data_pos[int(len(json_data_pos)/2)]['BusPosition']['PositionLat']#取中間一點的點會比較好 但實際號碼是亂碼 其實沒差
        posLon=json_data_pos[int(len(json_data_pos)/2)]['BusPosition']['PositionLon']#取中間一點的點會比較好 但實際號碼是亂碼 其實沒差
    
        for item in json_data_AQI:
            if item['Geometry']!=None:
                if item['Geometry']['COUNTYNAME']=='臺中市':
                    Dust2_5=int(item['Data']['Dust2_5'])*scale
                    dust_data+=[{'經緯':'%s,%s'%(str(item['LatLng']['lat']),str(item['LatLng']['lng'])),'位置':item['Geometry']['TOWNNAME'],'pm2.5':Dust2_5}]
        #print(dust_data)#偵錯

        for item in dust_data:
            map_ori_list+=[item['位置']]
        map_ori_list=list(set(map_ori_list))
        #print(map_ori_list)
        for item in map_ori_list:
            for item2 in dust_data:
                if item==item2['位置']:
                    map_ori+=item2['經緯']+'|'
                    break

        map_ori=map_ori[0:len(map_ori)-1]
        map_des='%s,%s'%(posLat,posLon)
        map_url='https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&mode=driving&language=zh-TW&key=AIzaSyD9ojwRyJKMDqorLnjpoaRT7s94S2EAkVA'%(map_ori,map_des)
        #print(map_url)
        res_map=requests.get(map_url)
        json_data_map=json.loads(res_map.text)

        for item in json_data_map['rows']:
            try:
                get_map+=[item['elements'][0]['distance']['value']]
            except KeyError as e3:
                get_map+=[9999999]
        get_map.index(min(get_map))

        for item in dust_data:
            if item['位置']==map_ori_list[get_map.index(min(get_map))]:
                Dust2_5=item['pm2.5']
                #print(map_ori_list[get_map.index(min(get_map))])偵錯
                #print(Dust2_5)偵錯
                break#一抓到位置相同即跳出迴圈

        if Dust2_5>100:
            ret=GAGA_SAY(3)
        elif Dust2_5>50:
            ret=GAGA_SAY(2)
        else:
            ret=GAGA_SAY(1)
    else:
        ret='目前沒有班車QQ 呱'

    return ret
def GAGA_SAY(select):
    rad=random.randint(0,2)
    word1=['是香香空氣呱!','出去玩嘎~','是藍天 是藍天~']
    word2=['空氣有點臭臭嘎...','想出去但臭臭空氣..','天空陰陰呱..']
    word3=['完全不敢出去了呱呱..!','口罩快給我呱!','這個雲好恐怖嘎!']
    if select==1:
        return word1[rad]
    elif select==2:
        return word2[rad]
    elif select==3:
        return word3[rad]

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

        headers=RES_HEAD(APPID,APPKey)

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
        line_bot_api.reply_message(
            event.reply_token,TextSendMessage(text='圖表正在製作中 呱呱!'))

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    loc='%s,%s'%(event.message.latitude,event.message.longitude)
    flex={
        "type": "imagemap",
        "baseUrl": "https://i.imgur.com/8nTHWOe.png?1",
        "altText": "This is an imagemap",
        "baseSize": {
            "width": 1040,
            "height": 170
            },
        "actions": [
            {
            "type": "message",
            "area": {
                "x": 2,
                "y": 4,
                "width": 520,
                "height": 166
            },
            "text": "/public_yes"
            },
            {
            "type": "message",
            "area": {
                "x": 522,
                "y": 0,
                "width": 518,
                "height": 170
                },
            "text": "/public_no"
            }
            ]
        }

    headers = {'Content-Type':'application/json','Authorization':'Bearer %s'%(line_token)}
    payload = {
        'replyToken':event.reply_token,
        'messages':[flex]
        }
    # res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,json=payload)

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

        headers=RES_HEAD(APPID,APPKey)

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

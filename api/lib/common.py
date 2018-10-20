#!/usr/bin/env python
import requests
import datetime  
import json
import random
import hmac
from hashlib import sha1
import base64
import time
import sys
import os
import configparser as ConfigParser
from math import sin, cos, sqrt, atan2, radians
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
from setting import *

class common(object):

    def __init__(self):
        None

# -------------------------------------------

    def detection_distance(self, center, around, max_distance):
        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(float(center['lat']))
        lon1 = radians(float(center['lon']))
        lat2 = radians(float(around['StopPosition']['PositionLat']))
        lon2 = radians(float(around['StopPosition']['PositionLon']))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        if distance < max_distance:
            return {"StopName": around['StopName']['Zh_tw'], "StopID": around['StopID'], "distance": distance}
        else:
            return None

    #製作驗證簽名
    def RES_HEAD(self, APPID, APPKey):
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
    def GET_SEC(self, time_str):
        h, m, s = time_str.split(':')
        try:
            sent=int(h) * 60 + int(m) 
        except ValueError as e1:
            sent=time_str
        return sent

    def DUST2_5_IS_WHAT(self, json_data_pos):
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
        
    def GAGA_SAY(self, select):
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

    def creat_stop_contents(self, center, max_distance):
        content = []
        max_count = 0
        with open("{}res/stop.json".format(FileRout),'rb') as f:
            data = json.load(f)
        for item in data:
            temp = self.detection_distance(center, item, 0.5)
            if temp != None and max_count < 25:
                content += [
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
                                "label": "%s" %temp['StopName'],
                                "uri": "https://linecorp.com"
                            },
                            "flex": 3
                            },
                            {
                            "type": "image",
                            "url": "https://i.imgur.com/ZZLbNkM.png"
                            },
                            {
                            "type": "text",
                            "text": "%s" %str(int(float(temp['distance'])*1000)),
                            "wrap": True,
                            "color": "#000000",
                            "gravity": "center",
                            "flex": 1
                            }
                        ]
                    }
                ]
                max_count += 1
        seen = set()
        new_content = []
        for d in content:
            key = d['contents'][0]['action']['label']
            if key not in seen:
                seen.add(key)
                new_content.append(d)
        new_content.sort(key = lambda key: float(key['contents'][2]['text']))
        for item in new_content:
            item['contents'][2]['text'] += 'm'

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
                    "contents": new_content,
                    "flex": 0
                }
            }
        }
        return flex

import sys
sys.path.append("../")
from setting import *
from model.apiGoogle import apiGoogle
from model.apiPtx import apiPtx
from model.processJson import processJson
from model.io import io
from model.common import common
import json
import uuid
import re

class lineContent(object):
    def __init__(self, google_map_key, file_route, app_id, app_key):
        self.apiGoogle = apiGoogle(google_map_key, file_route)
        self.apiPtx = apiPtx(app_id=app_id, app_key=app_key)
        self.processJson = processJson(file_route=FILE_ROUTE, global_query=GLOBAL)
        self.common = common()
        self.messages = list()
        self.io = io(file_route)
        self.text_message = {
            "type": "text",
            "text": ""
        }

    def getMessages(self):
        print(self.messages)
        return self.messages

    def clearMessages(self):
        self.messages = list()

    def flexBusInfo(self, bus_name, city, select="bus_num"):
        if select == "bus_num":
            self.messages.append(self.processJson.lineJson("bus_info", **{"bus_name": bus_name, "city": city}))

    def flexSetBusRoute(self, destination, city, user_id):
        flex = self.processJson.lineJson("nearby_place.flex")
        contents = list()
        bubble_contents = list()
        print(self.io.userActionPos(user_id))
        print(destination)
        json_data = self.apiGoogle.get("https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&language=zh-TW&transit_mode=bus&mode=transit&alternatives=true" %(self.io.userActionPos(user_id), destination))
        json_data['routes'].sort(key=lambda d:int(d['legs'][0]['duration']['value']))
        for item in json_data['routes']:
            for count, item2 in enumerate(item['legs'][0]['steps']):
                if count == 10: break
                if item2.get('transit_details'):
                    bubble_contents += [self.processJson.lineJson("set_bus_route.bus_contents",
                    **{
                        "text": item2['html_instructions'].replace('巴士','搭乘公車%s' %(item2['transit_details']['line']['short_name'])),
                        "bus_name": item2['transit_details']['line']['short_name'],
                        "city": city
                    })]
                else:
                    bubble_contents += [self.processJson.lineJson("set_bus_route.walk_contents",
                    **{
                        "text": item2['html_instructions'],
                        "ori_pos": "%s,%s" % (item2['start_location']['lat'], item2['start_location']['lng']),
                        "end_pos": "%s,%s" % (item2['end_location']['lat'], item2['end_location']['lng'])
                    })]
            contents += [self.processJson.lineJson("set_bus_route.contents",
            **{
                "text": "約%s" %(item['legs'][0]['duration']['text']),
                "contents": bubble_contents
            })]
            if len(json.dumps(flex) + json.dumps(contents)) < 50*1024:
                flex["contents"]["contents"] += contents 
            else:
                break
            bubble_contents = []
        self.io.userActionDelete(user_id)
        self.messages.append(flex)

    def flexNearbyPlace(self, google_data):
        flex = self.processJson.lineJson("nearby_place.flex")
        contents = list()
        for index, item in enumerate(google_data['results']):
            if index >= 10: break
            contents += [self.processJson.lineJson("nearby_place.contents",
            **{
                "url": item["image_name"],
                "name": item["name"],
                "ori_pos": google_data['origin'],
                "lat": str(item['geometry']['location']['lat']),
                "lon": str(item['geometry']['location']['lng'])
            })]
        flex["contents"]["contents"] += contents
        self.messages.append(flex)

    def flexSearchBusStop(self, stop_name):
        flex = self.processJson.lineJson("search_stop.flex")
        json_data = self.apiPtx.get("https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taichung?$select=RouteName&$filter=Stops/any(d:d/StopName/Zh_tw eq '%s')&$format=JSON" % stop_name)
        content = list()
        footer_contents = list()
        for item in json_data:
            content += [item['RouteName']['Zh_tw']]
        content = list(set(content))
        for i in range(0,len(content)-1): #有n-1回合(n為數字個數)
            for j in range(0,len(content)-1-i): #每回合進行比較的範圍
                if int(re.search('\d+',str(content[j])).group()) > int(re.search('\d+',str(content[j+1])).group()):
                    tmp = content[j]
                    content[j] = content[j+1]
                    content[j+1] = tmp
        for item in content:
            footer_contents += [self.processJson.lineJson("search_stop.footer_contents",
            **{
                "label": item,
                "text": item
            })]
        flex["contents"]["footer"]["contents"] = footer_contents
        self.messages.append(flex)

    def flexNearbyBusStop(self, location):
        location = {"lat": location.split(',')[0], "lon": location.split(',')[1]}
        flex = self.processJson.lineJson("nearby_stop.flex")
        footer_contents = list()
        contents = list()
        max_count = 0
        json_data = self.processJson.readJson("stop.json")
        for item in json_data:
            distance = self.common.detectionDistance(location, {"lat": item["StopPosition"]["PositionLat"],"lon": item["StopPosition"]["PositionLon"]})
            if distance < 0.5 and item["StopName"] not in [d["StopName"] for d in contents] and max_count < 25:
                contents += [{
                    "StopName": item["StopName"]['Zh_tw'],
                    "StopUID": item["StopUID"],
                    "distance": distance,
                    "StationPosition":{
                        "PositionLat":item["StopPosition"]['PositionLat'],
                        "PositionLon":item["StopPosition"]['PositionLon']
                    }
                }]
                max_count += 1
        contents.sort(key=lambda d:d['distance'])
        contents = [contents[item+1] for item in range(len(contents)-1) if item == 0 or contents[item]["StopName"] != contents[item+1]["StopName"]]# Get the first same item
        for item in contents:
            footer_contents += [self.processJson.lineJson("nearby_stop.footer_contents",
            **{
                "label": item["StopName"],
                "text": item["StopName"],
                "distance": "%sm" % str(int(item["distance"]*1000))
            })]
        flex["contents"]["footer"]["contents"] = footer_contents
        self.messages.append(flex)

    def flexNearbyBike(self, location):
        location = {"lat": location.split(',')[0], "lon": location.split(',')[1]}
        self.messages.append(
            self.processJson.lineJson("nearby_bike", **{"lat": location["lat"], "lon": location["lon"]})
        )

    def flexSetBusRouteConfirm(self, ori_pos, ori_user_id):
        self.io.checkUserRouteAction(ori_pos, ori_user_id)
        self.messages.append(self.processJson.lineJson("set_bus_route_confirm"))

    def textSetText(self, text):
        text_message = self.text_message
        text_message["text"] = text
        self.messages.append(text_message)

    def textWelcome(self):
        self.messages.append(self.processJson.lineJson("welcome.text"))

    def textGetWord(self, json_data):
        self.textSetText(self.processJson.randomWord(json_data["select"], json_data["word"]))
        return json_data["word"], json_data["city"], json_data["select"]

    def ImagemapWelcome(self):
        self.messages.append(self.processJson.lineJson("welcome.imagemap"))

    def ImagemapLocationMenu(self, line_event):
        self.messages.append(self.processJson.lineJson("location_menu",
        **{
            "lat": str(line_event.message.latitude),
            "lon": str(line_event.message.longitude)
        }))
import sys
sys.path.append("../")
from setting import *
from model.processJson import processJson
from model.apiPtx import apiPtx
import requests
import json

class bus(object):
    def __init__(self, file_route, global_query, app_id, app_key):
        self.apiPtx = apiPtx(app_id=app_id, app_key=app_key)
        self.processJson = processJson(file_route=file_route, global_query=global_query)

    def busPath(self, bus_name):
        ret = list()
        json_data = self.processJson.readJson("bus_path.json")
        for item in json_data:
            if item['RouteName']['Zh_tw'] == bus_name:
                ret += [item]
                if len(ret) >= 2 : break
        ret.sort(key=lambda d:int(d['Direction']))
        return ret

    def stopPos(self, bus_name, city, direction):
        res = self.apiPtx.get("https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/%s?$filter=RouteName/Zh_tw eq '%s' and Direction eq '%s'&$orderby=StopSequence asc&$format=JSON"%(city, bus_name, direction))
        select = list()
        ret = list()
        for item in res:
            select += [item['StopUID']]
        json_data = self.processJson.readJson("get_bus_pos.json")
        for item in json_data:
            if item['StopUID'] in select:
                ret += [item]
        for item in ret:
            for item2 in res:
                if item["StopUID"] == item2["StopUID"]:
                    item["PlateNumb"] = item2["PlateNumb"]
        return ret

    def busPos(self, json_data):
        bus_pos=[]
        sent_numb = "PlateNumb eq"
        for item in json_data:
            if item.get('PlateNumb') and item['PlateNumb'] != '' and item['PlateNumb'] not in bus_pos:
                bus_pos += [item['PlateNumb']]
                sent_numb += " '%s' or PlateNumb eq"%item['PlateNumb']
        sent_numb = sent_numb[0:len(sent_numb)-16]
        bud_pos=self.apiPtx.get("https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeByFrequency/City/Taichung?$filter=%s&$format=JSON"%sent_numb)
        print(bud_pos)
        for item in bud_pos:
            for item2 in json_data:
                if item2.get('PlateNumb') and item2['PlateNumb'] == item['PlateNumb']:
                    item2['BusPosition'] = item['BusPosition']
        return json_data

    def busStarAndEnd(self, bus_name):
        ret = list()
        json_data = self.processJson.readJson("get_bus_star_and_end.json")
        for item in json_data:
            if item['RouteName']['Zh_tw'] == bus_name:
                ret += [item]
        return ret

    def busAllNum(self):
        json_data = self.processJson.readJson("bus_all_num.json")
        json_data.sort(key=lambda d:int(d['RouteID']))
        return json_data

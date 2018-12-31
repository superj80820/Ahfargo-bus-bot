import sys
sys.path.append("../")
from setting import *
from model.apiPtx import apiPtx
from model.processJson import processJson
from model.common import common
import requests
import json

class bike(object):
    def __init__(self, app_id, app_key):
        self.apiPtx = apiPtx(app_id=app_id, app_key=app_key)
        self.processJson = processJson(file_route = FILE_ROUTE, global_query=GLOBAL)
        self.common = common()

    def realTime(self, lat, lon):
        ret = []
        json_data = self.processJson.readJson("bike.json")
        for item in json_data:
            distance = self.common.detectionDistance(ori_pos={"lat":lat,"lon":lon}, end_pos={"lat": item["StationPosition"]['PositionLat'],"lon": item["StationPosition"]['PositionLon']})
            if distance < 2:
                ret += [{
                    "StopName": item["StationName"]['Zh_tw'],
                    "StopUID": item["StationUID"],
                    "distance": distance,
                    "StationPosition":{
                        "PositionLat":item["StationPosition"]['PositionLat'],
                        "PositionLon":item["StationPosition"]['PositionLon']
                    }
                }]
        req_filter = str()
        for item in ret:
            req_filter += "StationUID eq '%s' or " %(item['StopUID'])
        req_filter = req_filter[0:len(req_filter)-4]
        print(req_filter)
        json_data = self.apiPtx.get("https://ptx.transportdata.tw/MOTC/v2/Bike/Availability/Taichung?$select=StationUID,AvailableRentBikes,AvailableReturnBikes&$filter=%s&$format=JSON"%(req_filter))
        for item in ret:
            for item2 in json_data:
                if item['StopUID'] == item2['StationUID']:
                    item['AvailableRentBikes'] = item2['AvailableRentBikes']
                    item['AvailableReturnBikes'] = item2['AvailableReturnBikes']
        return ret
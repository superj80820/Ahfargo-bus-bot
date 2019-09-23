import sys
sys.path.append("../")
from setting import *
import json
from model.processJson import processJson
from model.apiGoogle import apiGoogle
from model.io import io

class validation(object):
    def __init__(self, file_route, global_query):
        self.processJson = processJson(file_route = file_route, global_query=global_query)
        self.apiGoogle = apiGoogle(GOOGLE_MAP_KEY, FILE_ROUTE)
        self.io = io(file_route)

    def checkLineUserMessage(self, *args,**kwargs):
        data = self.processJson.readJson("bus_all_num.json")
        kwargs["select"]="default"
        for item in data:
            if kwargs["word"]==item['RouteName']['Zh_tw']:
                kwargs["select"]="bus_num"
                break
        return kwargs

    def checkLocation(self, line_event, location):
        json_data = self.apiGoogle.get('https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&language=zh-TW' %(str(float(line_event.message.latitude)),str(float(line_event.message.longitude))))
        local = json_data.get('plus_code').get('compound_code')
        if json_data["status"] != "ZERO_RESULTS":
            for item in location:
                if local.find(item) != -1: return True
        return False

    def checkUserRouteActionAgain(self, user_id):
        planing = self.io.userAction(user_id)
        print("ssssssss")
        print(planing)
        print("ssssssss")
        if planing == [('action',)]:
            return "in set"
        elif planing == []:
            print("ssssssss")
            return "in beging"
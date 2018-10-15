# coding: utf-8
import json
from math import sin, cos, sqrt, atan2, radians

def detection_distance(center, around, max_distance):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(24.162015)
    lon1 = radians(120.699098)
    lat2 = radians(float(around['StopPosition']['PositionLat']))
    lon2 = radians(float(around['StopPosition']['PositionLon']))

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    if distance < max_distance:
        return [around['StopName']['Zh_tw'], around['StopID'], distance]

ans = []

with open('res/stop.json','rb') as f:
    data = json.load(f)

for item in data:
    temp = detection_distance(item, item, 0.5)
    if temp != None:
        ans += [temp]
print(ans)

check = input('請輸入查詢公車號')
with open('res/test.json','rb') as f:
    data = json.load(f)
for item in data:
    if item['StopID']==check:
        print(item['RouteID'],item['Direction'])


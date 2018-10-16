# coding: utf-8
# 0: 去程, 1: 返程
from setting import *

ans = []

with open('res/stop.json','r') as f:
    data = json.load(f)

for item in data:
    temp = common().detection_distance(item, item, 0.5)
    if temp != None:
        ans += [temp]
print(ans)

# lat = str(24.162015)
# lon = str(120.699098)
# max_distance = str(500)
# headers=motc().get_headers()
# res=requests.get('http://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$select=StopName&$spatialFilter=nearby(StopPosition, %s, %s, %s)&$format=JSON' % (lat, lon, max_distance),headers=headers)
# print(res.json())
# print(len(res.json()))

ans = {}
ans['direction_0']=[]
ans['direction_1']=[]

check = "三川福德祠"
with open('res/test.json','r') as f:
    data = json.load(f)
for item in data:
    if item["StopName"]["Zh_tw"] == check:
        if item['Direction'] == 0:
            ans['direction_0'] += [{'StopID': item['StopID'], 'RouteID': item['RouteID'], 'Direction': item['Direction']}]
        elif item['Direction'] == 1:
            ans['direction_1'] += [{'StopID': item['StopID'], 'RouteID': item['RouteID'], 'Direction': item['Direction']}]
print(ans)


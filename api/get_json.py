import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)))))
from setting import *

# get_bus_pos
headers=common().RES_HEAD(APPID,APPKey)
res_pos=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$format=JSON",headers=headers)
json_data=json.loads(res_pos.text)
with open('%sres/get_bus_pos.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

# get_bus_star_and_end
headers=common().RES_HEAD(APPID,APPKey)
res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?$select=DepartureStopNameZh,DestinationStopNameZh&$format=JSON",headers=headers)
json_data=json.loads(res.text)
with open('%sres/get_bus_star_and_end.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

# bus_path
headers=common().RES_HEAD(APPID,APPKey)
res=requests.get("http://ptx.transportdata.tw/MOTC/v2/Bus/Shape/City/Taichung?$orderby=Direction asc&$format=JSON",headers=headers)
json_data=json.loads(res.text)
with open('%sres/bus_path.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

# bus_all_num
headers=common().RES_HEAD(APPID,APPKey)
res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?$select=RouteName,RouteID,SubRoutes&$format=JSON",headers=headers)
json_data=json.loads(res.text)
with open('%sres/bus_all_num.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

# stop
headers=common().RES_HEAD(APPID,APPKey)
res=requests.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$format=JSON",headers=headers)
json_data=json.loads(res.text)
with open('%sres/stop.json'% (FileRoute), 'w') as f:
    json.dump(json_data, f, indent=4, ensure_ascii=False)

# weather_place
res=requests.get("https://works.ioa.tw/weather/api/all.json")
json_data=json.loads(res.text)
for item in json_data:
    if item['name'] == '台中':
        with open('%sres/weather_place.json'% (FileRoute), 'w') as f:
            json.dump(item, f, indent=4, ensure_ascii=False)
        break

headers={
    'authorization': 'Bearer 91GhAd0IeyItMXs6e+Dl1sqYplxhXLMDj8ZzbnK57uqfgurw6IQ5TyjHoDd3S8XhPWVXWG9vKVtOBgGxYdRO8OhQpTbV93WakQi+uYnDgA4XroAAH/K5+FODaBAaTWG6VbDkrtgsVWnGgQBhBYmPNwdB04t89/1O/w1cDnyilFU=',
    'content-type': 'application/json'
}
payload={
    "to": "C9eb08306f28fd68ea5254ce123977be9",
    "messages":[
        {
            "type":"text",
            "text":"鴨發GO json檔案以更新"
        }
    ]
}
res=requests.post("https://api.line.me/v2/bot/message/push",headers=headers,data=json.dumps(payload))

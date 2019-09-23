# coding: utf-8

from setting import *
from model.apiPtx import apiPtx

apiPtxModel = apiPtx(app_id=APP_ID, app_key=APP_KEY)

# get_bus_pos
json_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$format=JSON")
with open('%sres/get_bus_pos.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_data, f)

# get_bus_star_and_end
json_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?&$format=JSON")
with open('%sres/get_bus_star_and_end.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_data, f)

# bus_path
json_data = apiPtxModel.get("http://ptx.transportdata.tw/MOTC/v2/Bus/Shape/City/Taichung?$orderby=Direction asc&$format=JSON")
with open('%sres/bus_path.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_data, f)

# bus_all_num
json_write = dict()
taichung_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taichung?$select=RouteName,RouteID,SubRoutes&$format=JSON")
taipei_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taipei?$select=RouteName,RouteID,SubRoutes&$format=JSON")
json_write["Taichung"] = taichung_data
json_write["Taipei"] = taipei_data
with open('%sres/bus_all_num.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_write, f)

# stop
json_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taichung?$format=JSON")
with open('%sres/stop.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_data, f)

# bike
json_data = apiPtxModel.get("https://ptx.transportdata.tw/MOTC/v2/Bike/Station/Taichung?$format=JSON")
with open('%sres/bike.json'% (FILE_ROUTE), 'w') as f:
    json.dump(json_data, f)

# weather_place
res=requests.get("https://works.ioa.tw/weather/api/all.json")
json_data=json.loads(res.text)
for item in json_data:
    if item['name'] == '台中':
        with open('%sres/weather_place.json'% (FILE_ROUTE), 'w') as f:
            json.dump(item, f)
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

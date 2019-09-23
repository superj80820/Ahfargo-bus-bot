import sys
sys.path.append("../../") 
from setting import *
from controller.lineContent import lineContentFlex
from controller.google import google
from core.route import route
import unittest

LINE_TOKEN = '91GhAd0IeyItMXs6e+Dl1sqYplxhXLMDj8ZzbnK57uqfgurw6IQ5TyjHoDd3S8XhPWVXWG9vKVtOBgGxYdRO8OhQpTbV93WakQi+uYnDgA4XroAAH/K5+FODaBAaTWG6VbDkrtgsVWnGgQBhBYmPNwdB04t89/1O/w1cDnyilFU='
route = route(LINE_TOKEN)
lineContentFlex = lineContentFlex(GOOGLE_MAP_KEY, FILE_ROUTE, APP_ID, APP_KEY)
google = google(GOOGLE_MAP_KEY, FILE_ROUTE)

# req = {"bus_name": "55","city": "Taichung"}
# route.use([
#     lineContentFlex.busInfo,
#     lineContentFlex.getMessages
#     ]).linePush("Ua594bce22e4cef7b0a70ecfaeb9c5d64", **req)
# req = {"location": "24.136862,120.685929"}
# route.use([
#     lineContentFlex.nearbyBike,
#     lineContentFlex.getMessages
#     ]).linePush("Ua594bce22e4cef7b0a70ecfaeb9c5d64", **req)
req = {"lat": "24.136862","lon": "120.685929"}
route.use([
    lineContentFlex.nearbyBusStop,
    lineContentFlex.getMessages
    ]).linePush("Ua594bce22e4cef7b0a70ecfaeb9c5d64", **req)

#!/usr/bin/env python
from setting import *
class common(object):

    def __init__(self):
        None

# -------------------------------------------

    def detection_distance(self, center, around, max_distance):
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
            return {"StopName": around['StopName']['Zh_tw'], "StopID": around['StopID'], "distance": distance}
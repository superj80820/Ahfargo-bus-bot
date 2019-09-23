# coding: utf-8
#!/usr/bin/env python
from math import sin, cos, sqrt, atan2, radians
import sqlite3 as sqlite

class common(object):
    def __init__(self):
        pass

    def detectionDistance(self, ori_pos, end_pos):
        # approximate radius of earth in km
        R = 6373.0
        print(ori_pos)
        lat1 = radians(float(ori_pos["lat"]))
        lon1 = radians(float(ori_pos["lon"]))
        lat2 = radians(float(end_pos["lat"]))
        lon2 = radians(float(end_pos["lon"]))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def getSec(self, time_str):
        """Time transform to min
        """
        h, m, s = time_str.split(':')
        try:
            sent=int(h) * 60 + int(m) 
        except ValueError as e1:
            sent=time_str
        return sent

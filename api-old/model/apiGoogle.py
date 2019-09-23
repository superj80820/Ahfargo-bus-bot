import sys
sys.path.append("../")
from setting import *
from model.common import common
import requests
import json
import uuid

class apiGoogle(object):
    def __init__(self, google_map_key, file_route = ''):
        self.common = common()
        self.google_map_key = google_map_key
        self.file_route = file_route

    def get(self, url):
        res = requests.get('%s&key=%s' % (url, self.google_map_key))
        try:
            return json.loads(res.text)
        except ValueError as e:
            return res

    def getGoogleMapImage(self, reference):
        res = self.get('https://maps.googleapis.com/maps/api/place/photo?maxheight=200&photoreference=%s' % reference)
        return res

    def nearbySearch(self, location, keyword="景點", radius="1000"):
        res = self.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=%s&location=%s&radius=%s&language=zh-TW' % (keyword, location, radius))
        return res

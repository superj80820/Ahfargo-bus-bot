import sys
sys.path.append("../")
from setting import *
from model.apiGoogle import apiGoogle
from model.io import io
import uuid

class google(object):
    def __init__(self, google_map_key, file_route=''):
        self.apiGoogle = apiGoogle(google_map_key, file_route)
        self.io = io(file_route)
        self.file_route = file_route

    def getAndSaveGoogleMapImage(self, location):
        res = self.apiGoogle.nearbySearch(location)
        res["origin"] = location
        for item in res['results']:
            uuid_name = str(uuid.uuid1())
            if item.get('photos'):
                self.io.saveImg(
                    '%sdata/image/%s.jpg' %(self.file_route, uuid_name),
                    self.apiGoogle.getGoogleMapImage(item['photos'][0]['photo_reference'])
                )
                item["image_name"] = uuid_name
            else:
                item["image_name"] = 'default'
        return res

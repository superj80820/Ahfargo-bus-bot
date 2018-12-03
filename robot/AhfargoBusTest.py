from exceptions import AssertionError
import json
import os
import requests
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")))
from setting import * 

class AhfargoBusTest(object):
    def __init__(self):
        self.HOST = "https://a805632f.ngrok.io/bus?RouteName="
        self.SESSION = requests.Session()
        self.SESSION.headers.update({
            "Content-Type": "application/json; charset=utf-8",
        })

    def __request(self, method, append=''):
        resp = self.SESSION.request(method, self.HOST + append)
        if resp.text == "":
            return resp.status_code
        else:
            return resp

# ---------------------------------------------------------------------------
    def bus_test(self, busNum):
        resp = self.__request('get', busNum + "&City=Taichung")
        return resp

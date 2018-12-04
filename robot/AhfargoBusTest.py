from exceptions import AssertionError
import json
import os
import requests
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../")))
from setting import * 

class AhfargoBusTest(object):
    def __init__(self):
        self.HOST = "http://127.0.0.1:5000/bus_path?bus_name="
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
    def bus_path(self, busNum):
        resp = self.__request('get', busNum)
        return resp

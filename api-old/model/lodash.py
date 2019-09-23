import sys
sys.path.append("../")
from setting import *

class lodash(object):
    def __init__(self):
        pass

    def dictByPath(self, json, path):
        keys = path.split('.')
        rv = json
        for key in keys:
            rv = rv[key]
        return rv
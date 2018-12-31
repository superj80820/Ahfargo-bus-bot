import sys
sys.path.append("../../")
from setting import *
from model.apiPtx import apiPtx
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.apiPtx = apiPtx(app_id=APP_ID, app_key=APP_KEY)

    def test_get(self):
        print("test get")
        self.assertTrue(self.apiPtx.get("http://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taichung?$top=30&$format=JSON"))

    def test_motcHead(self):
        print("test motcHead")
        self.assertTrue(self.apiPtx.motcHead())

if __name__ == '__main__':
    unittest.main()

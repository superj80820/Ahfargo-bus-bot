import sys
sys.path.append("../../")
from setting import *
from model.apiGoogle import apiGoogle
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.apiGoogle = apiGoogle(GOOGLE_MAP_KEY, FILE_ROUTE)

    def test_get(self):
        print(self._testMethodName)
        self.assertTrue(self.apiGoogle.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=景點&location=24.136862,120.685929&radius=1000&key=AIzaSyD9ojwRyJKMDqorLnjpoaRT7s94S2EAkVA&language=zh-TW"))

    def test_getGoogleMapImage(self):
        print(self._testMethodName)
        self.assertTrue(self.apiGoogle.getGoogleMapImage("CmRaAAAAzTAVELt7vWnDrVnqMKLAM5Qm-xe8TQDor30xPnV6tzHrQzeAdQ5kDjRCeL3jvXkZZkFcGFM-FqfFd9-jLR6jiRUXYIsvrVnOtYsZ3PbsH2lCY-3XQh9T-yXQxQ3fNebKEhD3g-JNrwjKfjGF4sCOkbm9GhShGqSHLeoTlShi7pmCrDTwwlTrkg"))

if __name__ == '__main__':
    unittest.main()

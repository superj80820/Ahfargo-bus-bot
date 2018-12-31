import sys
sys.path.append("../../") 
from setting import *
from controller.bike import bike
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.bike = bike(app_id=APP_ID, app_key=APP_KEY)

    def test_realTime(self):
        print("test realTime")
        self.assertTrue(self.bike.realTime(lat=24.136862, lon=120.685929))

if __name__ == '__main__':
    unittest.main()

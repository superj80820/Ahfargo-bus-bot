import sys
sys.path.append("../../") 
from setting import *
from controller.bus import bus
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.bus = bus(file_route=FILE_ROUTE, app_id=APP_ID, app_key=APP_KEY)

    def test_busPath(self):
        print("test busPath")
        self.assertTrue(self.bus.busPath('55'))

    def test_busPos(self):
        print("test busPos")
        self.assertTrue(self.bus.busPos('55',"Taichung", "1"))

    def test_busStarAndEnd(self):
        print("test busStarAndEnd")
        self.assertTrue(self.bus.busStarAndEnd('55'))

if __name__ == '__main__':
    unittest.main()

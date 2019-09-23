import sys
sys.path.append("../../") 
from setting import *
from model.processJson import processJson
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.processJson = processJson(file_route = FILE_ROUTE, global_query=GLOBAL)

    def test_randomWord(self):
        print("test randomWord")
        self.assertTrue(self.processJson.randomWord('bus_num'))
        self.assertTrue(self.processJson.randomWord('nearby_bus'))
        self.assertTrue(self.processJson.randomWord('nearby_bike'))
        self.assertTrue(self.processJson.randomWord('fun_place'))
        self.assertEqual(self.processJson.randomWord('default', "Hi"), "是在跟我說嗎呱?")
        self.assertTrue(self.processJson.randomWord('route_plan'))

if __name__ == '__main__':
    unittest.main()

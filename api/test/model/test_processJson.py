import sys
sys.path.append("../../")
from setting import *
from model.processJson import processJson
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.processJson = processJson(file_route=FILE_ROUTE, global_query=GLOBAL)

    def test_readJson(self):
        print(self._testMethodName)
        self.assertTrue(self.processJson.readJson("line_content.json"))

    def test_lineJson(self):
        print(self._testMethodName)
        self.assertTrue(self.processJson.lineJson("nearby_bike"))

if __name__ == '__main__':
    unittest.main()

import sys
sys.path.append("../../")
from setting import *
from model.common import common
from model.processJson import processJson
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.common = common()
        self.processJson = processJson(file_route = FILE_ROUTE, global_query=GLOBAL)

    def test_detectionDistance(self):
        print("test detectionDistance")
        self.assertEqual(self.common.detectionDistance(ori_pos={"lat":25.136862,"lon":120.685929}, end_pos={"lat":24.136862,"lon":120.685929}), 111.22983322959843)

if __name__ == '__main__':
    unittest.main()
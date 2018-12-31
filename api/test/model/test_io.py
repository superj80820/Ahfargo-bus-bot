import sys
sys.path.append("../../")
from setting import *
from model.io import io
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.io = io(file_route=FILE_ROUTE)

    def test_checkUserRouteAction(self):
        print("test get")
        self.io.checkUserRouteAction("asf","skmkmsss")

if __name__ == '__main__':
    unittest.main()

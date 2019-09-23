import sys
sys.path.append("../../")
from setting import *
from controller.google import google
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.google = google(GOOGLE_MAP_KEY, FILE_ROUTE)

    def test_getAndSaveGoogleMapImage(self):
        print(self._testMethodName)
        self.assertTrue(self.google.getAndSaveGoogleMapImage("24.136862,120.685929"))

if __name__ == '__main__':
    unittest.main()

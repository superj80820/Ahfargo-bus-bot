import sys
sys.path.append("../../")
from setting import *
from model.processJson import processJson
from controller.lineContent import lineContentFlex, lineContentText, lineContentImage
from controller.google import google
from jsonschema import validate
import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.google = google(GOOGLE_MAP_KEY, FILE_ROUTE)
        self.processJson = processJson(file_route=FILE_ROUTE, global_query=GLOBAL)
        self.schema_flex_carousel = self.processJson.readJson("schema/line_content.json")["flex_carousel"]
        self.schema_flex_bubble = self.processJson.readJson("schema/line_content.json")["flex_bubble"]
        self.schema_text = self.processJson.readJson("schema/line_content.json")["text"]
        self.schema_imagemap = self.processJson.readJson("schema/line_content.json")["imagemap"]
        self.lineContentFlex = lineContentFlex(google_map_key=GOOGLE_MAP_KEY, file_route=FILE_ROUTE, app_id=APP_ID, app_key=APP_KEY)
        self.lineContentText = lineContentText(google_map_key=GOOGLE_MAP_KEY, file_route=FILE_ROUTE, app_id=APP_ID, app_key=APP_KEY)
        self.lineContentImage = lineContentImage(google_map_key=GOOGLE_MAP_KEY, file_route=FILE_ROUTE, app_id=APP_ID, app_key=APP_KEY)

    def test_lineContentFlex_setBusRoute(self):
        print(self._testMethodName)
        self.lineContentFlex.setBusRoute("24.136862,120.685929", "24.1798677,120.6023033", "Taichung")
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_carousel)

    def test_lineContentFlex_setBusRouteConfirm(self):
        print(self._testMethodName)
        self.lineContentFlex.setBusRouteConfirm("24.136862,120.685929", "superj80820")
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_bubble)

    def test_lineContentFlex_nearbyBusStop(self):
        print(self._testMethodName)
        self.lineContentFlex.nearbyBusStop({"lat":"24.136862","lon":"120.685929"})
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_bubble)

    def test_lineContentFlex_nearbyPlace(self):
        print(self._testMethodName)
        google_data = self.google.getAndSaveGoogleMapImage("24.136862,120.685929")
        self.lineContentFlex.nearbyPlace(google_data)
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_carousel)

    def test_lineContentFlex_busInfo(self):
        print(self._testMethodName)
        self.lineContentFlex.busInfo("55", "Taichung")
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_bubble)

    def test_lineContentFlex_nearbyBike(self):
        print(self._testMethodName)
        self.lineContentFlex.nearbyBike("24.136862,120.685929")
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_bubble)

    def test_lineContentText_setText(self):
        print(self._testMethodName)
        self.lineContentText.setText("Hi 你好")
        validate(self.lineContentText.getMessages()[0], self.schema_text)

    def test_lineContentImage_welcome(self):
        print(self._testMethodName)
        self.lineContentImage.welcome()
        validate(self.lineContentImage.getMessages()[0], self.schema_imagemap)

    def test_lineContentFlex_searchBusStop(self):
        print(self._testMethodName)
        self.lineContentFlex.searchBusStop("中央市場")
        validate(self.lineContentFlex.getMessages()[0], self.schema_flex_bubble)

if __name__ == '__main__':
    unittest.main()

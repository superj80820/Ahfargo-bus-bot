from django.test import TestCase
from busApi.services import ptxApi
from django.conf import settings
from jsonschema import validate
import json
import os

class busApiTestCase(TestCase):
    def setUp(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/schema.json' , 'r') as schema:
            self.schema = json.loads(schema.read())
        self.objPtxApi = ptxApi(ptxId = settings.PTX_ID, ptxKey = settings.PTX_KEY)

    def testPtxApiGet(self):
        schema = self.schema["get"]
        self.assertEqual(
            validate(instance = self.objPtxApi.get('http://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taichung?$top=30&$format=JSON'), schema = schema),
            None
        )
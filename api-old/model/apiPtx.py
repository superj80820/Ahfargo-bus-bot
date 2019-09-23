import requests
import json
import datetime
import hmac
from hashlib import sha1
import base64

class apiPtx(object):
    def __init__(self, app_id, app_key):
        self.app_id=app_id
        self.app_key=app_key

    def get(self, url):
        headers = self.motcHead()
        res=requests.get(url, headers=headers)
        return json.loads(res.text)

    def motcHead(self):
        X_Date=datetime.datetime.now(datetime.timezone.utc).strftime("%a, "+"%d %b "+"%Y %H:%M:%S"+" GMT")
        print(X_Date)

        sent_app_key = str.encode(self.app_key)
        sent_time = str.encode("x-date: "+X_Date)
        hmac_ans = hmac.new(sent_app_key,sent_time ,sha1)
        hmac_ans=base64.b64encode(hmac_ans.digest())
        hmac_ans=str(hmac_ans)[2:len(str(hmac_ans))-1]
        print(hmac_ans)

        Authorization='hmac username="'+self.app_id+'", algorithm="hmac-sha1", headers="x-date", signature="'+hmac_ans+'"'
        headers={ 'Authorization': Authorization, 'X-Date':X_Date}

        return headers
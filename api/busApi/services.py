import requests
import json
import datetime
import hmac
from hashlib import sha1
import base64

class ptxApi(object):
    def __init__(self, ptxId, ptxKey):
        '''
		Parameters:
			ptxId: String
				- PTX id
			ptxKey: String
				- PTX key
		'''
        self.ptxId=ptxId
        self.ptxKey=ptxKey

    def __motcHead(self):
        X_Date=datetime.datetime.now(datetime.timezone.utc).strftime("%a, "+"%d %b "+"%Y %H:%M:%S"+" GMT")

        sent_ptxKey = str.encode(self.ptxKey)
        sent_time = str.encode("x-date: "+X_Date)
        hmac_ans = hmac.new(sent_ptxKey,sent_time ,sha1)
        hmac_ans=base64.b64encode(hmac_ans.digest())
        hmac_ans=str(hmac_ans)[2:len(str(hmac_ans))-1]

        Authorization='hmac username="'+self.ptxId+'", algorithm="hmac-sha1", headers="x-date", signature="'+hmac_ans+'"'
        headers={ 'Authorization': Authorization, 'X-Date':X_Date}

        return headers

    def get(self, url):
        res=requests.get(url, headers = self.__motcHead())
        return json.loads(res.text)

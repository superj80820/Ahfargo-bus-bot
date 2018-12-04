#!/usr/bin/env python
from setting import *

class motc(object):

    def __init__(self):
        None
        
# -------------------------------------------

    def get_headers(self):
        X_Date=datetime.datetime.now(datetime.timezone.utc).strftime("%a, "+"%d %b "+"%Y %H:%M:%S"+" GMT")
        print(X_Date)

        sent_APPKey = str.encode(APPKey)
        sent_time = str.encode("x-date: "+X_Date)
        hmac_ans = hmac.new(sent_APPKey,sent_time ,sha1)
        hmac_ans=base64.b64encode(hmac_ans.digest())
        hmac_ans=str(hmac_ans)[2:len(str(hmac_ans))-1]
        print(hmac_ans)

        Authorization='hmac username="'+APPID+'", algorithm="hmac-sha1", headers="x-date", signature="'+hmac_ans+'"'

        headers={ 'Authorization': Authorization, 'X-Date':X_Date}
        return headers    

    
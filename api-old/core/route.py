# coding: utf-8

import requests
import json
from flask import jsonify

class route(object):
    def __init__(self, line_token):
        self.func_list = list()
        self.line_token = line_token

    def use(self, func):
        self.func_list += [func]
        return self

    def handle(self, **req):
        ret = self.func_list[0](**req)
        for func in self.func_list[1:]:
            ret = func() if ret is None else func(*ret) if type(ret) is tuple else func(ret)
        self.func_list = list()
        return ret

    def lineReply(self, reply_token, **req):
        messages = self.handle(**req)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s'%(self.line_token)
        }
        print(json.dumps(messages))
        payload = {
            'replyToken': reply_token,
            'messages': messages
        }
        res=requests.post('https://api.line.me/v2/bot/message/reply',headers=headers,data=json.dumps(payload))
        print(res.text)

    def linePush(self, to, **req):
        messages = self.handle(**req)
        headers={
            'authorization': 'Bearer %s'%(self.line_token),
            'content-type': 'application/json'
        }
        payload={
            "to": to,
            "messages": messages
        }
        res=requests.post("https://api.line.me/v2/bot/message/push",headers=headers,data=json.dumps(payload))
        print(res.text)

    def reply(self, **req):
        messages = self.handle(**req)
        return jsonify(messages)
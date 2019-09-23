import json
import random
import re
from model.common import common
from model.lodash import lodash


class processJson(object):
    def __init__(self, file_route, global_query):
        self.file_route = file_route
        self.lodash = lodash()
        self.global_query = global_query

    def randomWord(self, select, word=None):
        json_data = self.readJson("get_word.json")
        if select == 'default':
            for item in json_data[select]:
                for item2 in item['schema']:
                    if word.find(item2) != -1: return item['word']
            return None
        else:
            return json_data[select][random.randint(0,len(json_data[select])-1)]

    def lineJson(self, path, **query):
        json_data = self.readJson("line_content.json")
        json_data = self.lodash.dictByPath(json_data, path)
        print("All query: %s" % str(re.findall('\${.*?\}', json.dumps(json_data))))
        query.update(self.global_query)
        for name, value in query.items():
            if isinstance(value, str):
                json_data = json.loads(json.dumps(json_data).replace('${%s}' % name, value))
            else:
                json_data = json.loads(json.dumps(json_data).replace('"${%s}"' % name, json.dumps(value)))
        return json_data

    def readJson(self, file):
        with open("{}res/{}".format(self.file_route, file), encoding="utf-8") as f:
            json_data = json.load(f)
        return json_data

    def jsonSchema(self):
        pass
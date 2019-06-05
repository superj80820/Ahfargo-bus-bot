import fileinput
import sys, os
import requests
import re
from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv
dotenv = load_dotenv(dotenv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../.env'))

def replaceAll(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def getAllfilesPath(path):
    return ['{}/{}'.format(path, f) for f in listdir(path) if isfile(join(path, f))]

def updateLIFF(content, url):
    mapping = {'LIFF_BUS': 'bus_list_demo.html', 'LIFF_BIKE': 'bikedemo'}
    liffId = re.search('app/(.*)', os.getenv(content)).group(1)
    headers = {
        'authorization': 'Bearer {}'.format(os.getenv('LINE_TOKEN')),
        'content-type': 'application/json'
    }
    payload = {
        "view":{
            "type": "tall",
            "url": '{}/{}'.format(url, mapping[content])
        }
    }
    res = requests.put('https://api.line.me/liff/v1/apps/{}'.format(liffId), headers = headers, json = payload)
    assert (res.status_code != 204)

if __name__ == '__main__':
    print('Start init')
    for item in getAllfilesPath('../web/assets/js'):
        replaceAll(item, 'APP_URL', os.getenv('APP_URL'))
    for item in getAllfilesPath('../web'):
        replaceAll(item, 'GOOGLE_MAP_KEY', os.getenv('GOOGLE_MAP_KEY'))
    updateLIFF('LIFF_BUS', os.getenv('WEB_URL'))
    updateLIFF('LIFF_BIKE', os.getenv('WEB_URL'))
    print('Done init')
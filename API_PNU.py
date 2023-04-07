# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# pip install requests
import requests

import json

# server URL
api_url = "http://api.vworld.kr/req/search"

# read api key
api_key = "API KEY"

paramDict = {
    'service': 'search',
    'request': 'search',
    'version': '2.0',
    'crs': 'EPSG:900913',
#    'bbox': '14140071.146077,4494339.6527027,14160071.146077,4496339.6527027',
    'size': 10,
    'page': 1,
    'query': '전주시 덕진구 농생명로 300 농촌진흥청',
    'type': 'address',
    'category': 'road',
    'format': 'json',
    'errorformat': 'json',
    'key': api_key
}

print(api_url)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers, params=paramDict)

json_obj = json.loads(response.text)

# response body
print("도로주소: " + json_obj['response']['result']['items'][0]['address']['road'])
print("PNU: " + json_obj['response']['result']['items'][0]['id'])
print("x좌표: " + json_obj['response']['result']['items'][0]['point']['x'])
print("y좌표: " + json_obj['response']['result']['items'][0]['point']['y'])

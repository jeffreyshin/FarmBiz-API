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
api_key = input("vworld 인증키를 입력하세요: ")

paramDict = {
    'service': 'search',
    'request': 'search',
    'version': '2.0',
    'crs': 'EPSG:900913',
#    'bbox': '14140071.146077,4494339.6527027,14160071.146077,4496339.6527027',
    'size': 10,
    'page': 1,
    'query': '완주군 이서면 금평리 155',
    'type': 'address',
    'category': 'parcel',
    'format': 'json',
    'errorformat': 'json',
    'key': api_key
}

print(api_url)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers, params=paramDict)

json_obj = json.loads(response.text)
print(response.text)

# response body
if json_obj['response']['status'] == 'OK':
    print("도로주소: " + json_obj['response']['result']['items'][0]['address']['parcel'])
    print("PNU: " + json_obj['response']['result']['items'][0]['id'])
    print("x좌표: " + json_obj['response']['result']['items'][0]['point']['x'])
    print("y좌표: " + json_obj['response']['result']['items'][0]['point']['y'])

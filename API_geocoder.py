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
api_url = "http://api.vworld.kr/req/address"

# read api key
api_key = "API_KEY"

paramDict = {
    "service": "address",
    "request": "getcoord",
    "crs": "epsg:4326",
    "address": "판교로 242",
    "format": "json",
    "type": "road",
    "key": api_key
}

print(api_url)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers, params=paramDict)

json_obj = json.loads(response.text)
print(response.text)

# response body
if json_obj['response']['status'] == 'OK':
    print("x좌표: " + json_obj['response']['result']['point']['x'])
    print("y좌표: " + json_obj['response']['result']['point']['y'])

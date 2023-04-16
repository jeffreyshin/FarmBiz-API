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
api_url = "http://apis.data.go.kr/1390906/thiForecastApi_gong"

# api key
api_key = "API KEY"

api_uri = f"{api_url}/getList_thiForecastApi"
print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'nx': 55,
    'ny': 127
}
# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)
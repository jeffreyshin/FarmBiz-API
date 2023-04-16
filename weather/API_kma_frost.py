# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# pip install requests

# server URL
api_url = "http://apis.data.go.kr/1360000/FrstFcstInfoService/getFrstOcurFcst"

# read api key
api_key = "API KEY"

paramDict = {
    'serviceKey': api_key,
    'pageNo' : '1',
    'numOfRows' : '10',
    'dataType' : 'json',
    'BASE_DATE' : '20230121',
    'BASE_TIME' : '0500',
    'LAT' : '36.5',
    'LON' : '128.0'
}

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers, params=paramDict)

# response body
print(response.text)

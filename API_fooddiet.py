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
api_url = "http://apis.data.go.kr/1390802/AgriFood/FdFoodCkryImage"

# read api key
api_key = "API KEY"

api_uri = f"{api_url}/getKoreanFoodFdFoodCkryImageList"

print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'service_Type': 'xml',
    'Page_No': 1,
    'Page_Size': 1,
    'food_Name': '김치',
    'ckry_Name': '조리'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)

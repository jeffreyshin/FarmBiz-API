# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# server URL
api_url = "http://apis.data.go.kr/1390802/SoilEnviron/SoilCharacSctnn"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}/getSoilCharacterSctnn"

print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'PNU_Code': '4215034022100050000'
}
# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)
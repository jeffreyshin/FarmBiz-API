# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# server URL
api_url = "http://www.naas.go.kr/unityapi/service/byPass/SoilEnviron/waterPrscrptn"

# read api key
api_key = "API KEY"

api_uri = f"{api_url}/getWaterPrscrptn"

paramDict = {
    'SG_APIM': api_key,
    'view_Cd': 'WS0095',
    'vapour_Stad_Gbn': '01',
    'mth_Cd': '01',
    'in_House': 100
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)



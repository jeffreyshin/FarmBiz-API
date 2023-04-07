# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request

# pip install requests
import requests

import json

# server URL
api_url = "http://apis.data.go.kr/1390802/SoilEnviron/FrtlzrUseExp"

# read api key
api_key = "API KEY"

api_uri = f"{api_url}/getSoilFrtlzrExprnRiceInfo"

paramDict = {
    'serviceKey': api_key,
    'PNU_Code': '4215034022100050000',
    'crop_Code': '00001',
    'rice_Qlt_Code': '1',
    'acid': 6.2,
    'om': 25,
    'vldpha': 5,
    'posifert_K': 5,
    'posifert_Ca': 5,
    'posifert_Mg': 10,
    'vldsia': 30,
    'selc=': 6,
    'limeamo': 15,
    'nit': 5,
    'cec': 10,
    'ammo': 5,
    'animix_Ratio_Cattl': 28,
    'animix_Ratio_Pig': 22,
    'animix_Ratio_Chick': 19
}

print(api_uri)
# request url

headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)

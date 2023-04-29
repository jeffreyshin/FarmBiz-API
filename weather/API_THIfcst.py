# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests
import xmltodict

# pip install requests
import requests

import json

# server URL
api_url = "http://apis.data.go.kr/1390906/thiForecastApi_gong"

# api key
api_key = input("인증키를 입력하세요: ")

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
#print(response.text)

dict_obj = xmltodict.parse(response.text)
json_obj = json.dumps(dict_obj)
#print(json_obj)

# response body
if dict_obj['response']['header']['resultCode'] == "200":
    for k in range(0, int(len(dict_obj['response']['body']['items']['item']))):
        print()
        print("=========================")
        print("forcast date:", dict_obj['response']['body']['items']['item'][k]['fcstDate'])
        print("forecast time:", dict_obj['response']['body']['items']['item'][k]['fcstTime'])
        print("sky:", dict_obj['response']['body']['items']['item'][k]['sky'])
        print("t3h:", dict_obj['response']['body']['items']['item'][k]['t3h'])
        print("pop:", dict_obj['response']['body']['items']['item'][k]['pop'])
        print("reh:", dict_obj['response']['body']['items']['item'][k]['reh'])
        print("thi:", dict_obj['response']['body']['items']['item'][k]['thi'])

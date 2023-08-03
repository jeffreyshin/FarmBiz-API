# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests
import datetime as dt

# pip install requests

# server URL
api_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0"

# read api key

api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}/getVilageFcst"

dt_now = dt.datetime.now()
date = dt.datetime.strftime(dt_now, "%Y%m%d")
time = dt.datetime.strftime(dt_now, "%H00")
# if time == "0000":
time = "0800"


paramDict = {
    'serviceKey': api_key,
    'numOfRows': 200,
    'pageNo': 4,
    'dataType': 'json',
    'base_date': date,
    'base_time': time,
    'nx': 38,
    'ny': 127
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
print(response.text)
dict_obj = response.json()
print(dict_obj)

if dict_obj['response']['header']['resultCode'] == "00":
    print("basetime:", dict_obj['response']['body']['items']['item'][0]['baseDate'], \
          dict_obj['response']['body']['items']['item'][0]['baseTime'])
    for i in range(0, int(len(dict_obj['response']['body']['items']['item']))):
        print("forecast time:", dict_obj['response']['body']['items']['item'][i]['fcstDate'], \
              dict_obj['response']['body']['items']['item'][i]['fcstTime'], \
              dict_obj['response']['body']['items']['item'][i]['category'], \
              dict_obj['response']['body']['items']['item'][i]['fcstValue'])


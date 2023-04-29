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

# server URL
api_url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"

# read api key
api_key = input("인증키를 입력하세요: ")

paramDict = {
    'serviceKey': api_key,
    'numOfRows': 10,
    'pageNo': 1,
    'dataCd': 'ASOS',
    'dateCd': 'DAY',
    'startDt': '20100101',
    'endDt': '20100105',
    'stnIds': 119
}

print(api_url)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers, params=paramDict)

# response body
#print(response.text)

json_obj = xmltodict.parse(response.text)

#print(json_obj)

# response body
if json_obj['response']['header']['resultCode'] == '00':
    print("지역: " + json_obj['response']['body']['items']['item'][0]['stnNm'])
    print("날짜: " + json_obj['response']['body']['items']['item'][0]['tm'])
    print("평균기온: " + json_obj['response']['body']['items']['item'][0]['avgTa'])
    print("최저기온: " + json_obj['response']['body']['items']['item'][0]['minTa'])
    print("최고기온: " + json_obj['response']['body']['items']['item'][0]['maxTa'])
    print("평균상대습도: " + json_obj['response']['body']['items']['item'][0]['avgRhm'])

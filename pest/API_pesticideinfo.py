# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests
import xmltodict

# server URL
api_url = "https://psis.rda.go.kr/openApi/service.do"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}"

paramDict = {
    'apiKey': api_key,
    'serviceCode': 'SVC01',
    'serviceType': 'AA001',
    'startPoint': 1,
    'displayCount': 500,
    'cropName' : '고추',
    'cropCheck': 'Y',
    'diseaseWeedName' : '탄저병'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)
print(response.text)

json_obj = xmltodict.parse(response.text)

print(json_obj)


for i in range(0, int(json_obj['service']['totalCount'])):
    print(i, "---------------------- ")
    print(json_obj['service']['list']['item'][i]['cropName'])
    print(json_obj['service']['list']['item'][i]['diseaseWeedName'])
    print(json_obj['service']['list']['item'][i]['useName'])
    print(json_obj['service']['list']['item'][i]['pestiKorName'])
    print(json_obj['service']['list']['item'][i]['pestiBrandName'])
    print(json_obj['service']['list']['item'][i]['compName'])

# response body



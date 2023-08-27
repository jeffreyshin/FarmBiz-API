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
api_url = "http://ncpms.rda.go.kr/npmsAPI/service"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}"

paramDict = {
    'apiKey': api_key,
    'serviceCode': 'SVC51',
    'cropName' : '벼'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
# response = requests.get(api_uri, headers=headers, params=paramDict)
response = requests.get(api_uri, params=paramDict)
# print(response.text)

json_obj = xmltodict.parse(response.text)

# print(json_obj)
# print(json.dumps(json_obj, indent = 4, sort_keys = True))

for i in range(0, int(len(json_obj['service']['list']['item']))):
    if json_obj['service']['list']['item'][i]['kncrNm'] == '논벼'  and \
            json_obj['service']['list']['item'][i]['examinYear'] == '2022':
           # json_obj['service']['list']['item'][i]['insectKey'] == '202200204FC01010101322005':
        print(i, "---------------------- ")
        # print(json_obj['service']['list']['item'][i]['examinSpchcknCode'])
        print(json_obj['service']['list']['item'][i]['examinSpchcknNm'])
        print(json_obj['service']['list']['item'][i]['examinTmrd'])
        print(json_obj['service']['list']['item'][i]['examinYear'])
        print(json_obj['service']['list']['item'][i]['inputStdrDatetm'])
        print(json_obj['service']['list']['item'][i]['insectKey'])
        # print(json_obj['service']['list']['item'][i]['kncrCode'])
        print(json_obj['service']['list']['item'][i]['kncrNm'])
        # print(json_obj['service']['list']['item'][i]['predictnSpchcknCode'])
        print(json_obj['service']['list']['item'][i]['predictnSpchcknNm'])



# response body



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
    # 'serviceType': 'AA001'
    # 'cropName': '논벼',
    # 'sickNameKor': '깨씨무늬병'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
# response = requests.get(api_uri, headers=headers, params=paramDict)
response = requests.get(api_uri, params=paramDict)
# print(response.text)

json_obj = xmltodict.parse(response.text)

# print(json.dumps(json_obj, indent = 4, sort_keys = True))

##################################################
list_insect = []
list_surveyDate = []

for i in range(0, int(len(json_obj['service']['list']['item']))):
    if json_obj['service']['list']['item'][i]['kncrNm'] == '논벼' and \
            json_obj['service']['list']['item'][i]['examinYear'] == '2023':
        print(i, "---------------------- ")
        # print(json_obj['service']['list']['item'][i]['predictnSpchcknNm'])
        # print(json_obj['service']['list']['item'][i]['inputStdrDatetm'])
        list_insect.append(json_obj['service']['list']['item'][i]['insectKey'])
        list_surveyDate.append(json_obj['service']['list']['item'][i]['inputStdrDatetm'])


sido_code = 45
ii = 0

for insect_key in list_insect:
    paramDict2 = {
        'apiKey': api_key,
        'serviceCode': 'SVC53',
        'serviceType': 'AA001',
        'insectKey': insect_key,
        'sidoCode': sido_code
    }
    response2 = requests.get(api_uri, params=paramDict2)
    # print(response2.text)
    json_obj2 = xmltodict.parse(response2.text)

    # print(json.dumps(json_obj2, indent = 4, sort_keys = True))

    print(int(len(json_obj2['service']['list'])))
    print(list_surveyDate[ii], json_obj2['service']['insectKey'], json_obj2['service']['examinTmrd'], \
          json_obj2['service']['examinSpchcknNm'])

    l = json_obj2['service']['list']
    # print(l)
    l = l.replace("=", ":")
    l = l.replace("inqireValue", "\"inquireValue\"")
    l = l.replace("inqireCnClCode", "\"inqireCnClCode\"")
    l = l.replace("pageUnit", "\"pageUnit\"")
    l = l.replace("pageIndex", "\"pageIndex\"")
    l = l.replace("pageSize", "\"pageSize\"")
    l = l.replace("sidoNm", "\"sidoNm\"")
    l = l.replace("sidoCode", "\"sidoCode\"")
    l = l.replace("dbyhsNm", "\"dbyhsNm\"")
    l = l.replace("sigunguNm", "\"sigunguNm\"")
    l = l.replace("sigunguCode", "\"sigunguCode\"")
    l = l.replace(":", ":\"")
    l = l.replace("},", "\"},")
    l = l.replace(", \"", "\", \"")
    l = l.replace("}]", "\"}]")

    # print(l)

    dict = eval(l)

    for i in range(0, len(dict)):
        if float(dict[i]['inquireValue']) > 0:
            print(dict[i]['sigunguNm'], dict[i]['dbyhsNm'], str(dict[i]['inquireValue']))

    print("==========================")
    ii = ii+1

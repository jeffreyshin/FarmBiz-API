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
api_url = "http://apis.data.go.kr/B552149/reserviorWaterLevel"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}/reservoircode/"

print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'county': '충청남도 논산시',
    'fac_name': '탑정',
     'pageNo': 1,
    'numOfRows': 10
}
# request url
headers = {'Accept': 'application/xml; charset=utf-8', 'Content-Type': 'application/xml; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)
#response = requests.get(api_uri, params=paramDict)

# response body
print(response.text)

json_obj = xmltodict.parse(response.text)
print(json_obj)

fac_code = json_obj['response']['body']['item']['fac_code']
print(fac_code)

paramDict = {
    'serviceKey': api_key,
    'fac_code': fac_code,
    'pageNo': 1,
    'numOfRows': 50,
    'date_s': '20220901',
    'date_e': '20220931'
}
api_uri = f"{api_url}/reservoirlevel/"

response = requests.get(api_uri, headers=headers, params=paramDict)
#response = requests.get(api_uri, params=paramDict)

# response body
print(response.text)
json_obj = xmltodict.parse(response.text)
print(json_obj)

for i in range(0, 30):
    print("저수지 이름: " + json_obj['response']['body']['item'][i]['fac_name'])
    print("측정날짜: " + json_obj['response']['body']['item'][i]['check_date'])
    print("저수지 수위: " + json_obj['response']['body']['item'][i]['water_level'])
    print("저수율: " + json_obj['response']['body']['item'][i]['rate'])
    print("------------")


# response body
'''
print("시료채취년도: " + json_obj['response']['body']['items']['item']['Any_Year'])
print("토양검정일: " + json_obj['response']['body']['items']['item']['Exam_Day'])
print("주소: " + json_obj['response']['body']['items']['item']['PNU_Nm'])
print("pH: " + json_obj['response']['body']['items']['item']['ACID'])
print("유기물: " + json_obj['response']['body']['items']['item']['OM'])
print("유효인산: " + json_obj['response']['body']['items']['item']['VLDPHA'])
print("유효규산: " + json_obj['response']['body']['items']['item']['VLDSIA'])
print("마그네슘: " + json_obj['response']['body']['items']['item']['POSIFERT_MG'])
print("칼륨: " + json_obj['response']['body']['items']['item']['POSIFERT_K'])
print("칼슘: " + json_obj['response']['body']['items']['item']['POSIFERT_CA'])
print("전기전도도: " + json_obj['response']['body']['items']['item']['SELC'])


'''


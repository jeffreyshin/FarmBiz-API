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
api_url = "http://apis.data.go.kr/1390802/SoilEnviron/SoilExam"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}/getSoilExam"

print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'PNU_Code': '4571033023101550000'
}
# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
#print(response.text)

json_obj = xmltodict.parse(response.text)
#print(json_obj)

# response body
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


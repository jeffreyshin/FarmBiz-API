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
api_url = "http://apis.data.go.kr/1390802/AgriWeather/WeatherObsrInfo/InsttWeather/getWeatherTimeList"

# read api key
api_key = "API_KEY"

paramDict = {
    'serviceKey': api_key,
    'Page_No': 1,
    'Page_Size': 50,
    'date_Time': '2023-04-02',
    'obsr_Spot_Nm': '광주시 목현동',
    'obsr_Spot_Code': '464030A001'
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
print("지역: " + json_obj['response']['body']['items']['item'][0]['obsr_Spot_Nm'])
if json_obj['response']['header']['result_Code'] == '200':
    for i in range(0, int(json_obj['response']['body']['total_Count'])):
        print("\n관측시각: " + json_obj['response']['body']['items']['item'][i]['date_Time'])
        print("기온(1.5m): " + json_obj['response']['body']['items']['item'][i]['tmprt_150'])
        print("일사량: " + json_obj['response']['body']['items']['item'][i]['solrad_Qy'])
        print("토양수분(30cm): " + json_obj['response']['body']['items']['item'][i]['soil_Mitr_30'])

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# pip install requests
import requests

import json
import xmltodict

# server URL
api_url = "https://apis.data.go.kr/1390802/AgriFood/NationStdFood/V3"

# read api key
api_key = input("인증키를 입력하세요: ")

api_uri = f"{api_url}/getKoreanFoodNationStdList"

paramDict = {
    'serviceKey': api_key,
    'Page_No': 6,
    'Page_Size': 20,
    'fd_Grupp': 'A'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)
#print(response.text)
dict_obj = xmltodict.parse(response.text)
json_obj = json.dumps(dict_obj)
print(json_obj)

if dict_obj['response']['header']['result_Code'] == "200":
    for i in range(0, int(dict_obj['response']['body']['rcdcnt'])):
        print(dict_obj['response']['body']['items']['item'][i]['food_Nm'])
        print(dict_obj['response']['body']['items']['item'][i]['food_Code'])

#################################################

api_uri = f"{api_url}/getKoreanFoodNationStdIdntList"

paramDict = {
    'serviceKey': api_key,
    'food_Code': 'A0160080005a'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
#print(response.text)

dict_obj = xmltodict.parse(response.text)
json_obj = json.dumps(dict_obj)
#print(json_obj)

# response body
if dict_obj['response']['header']['result_Code'] == "200":
    print("###########################")
    print("food_Code: " + dict_obj['response']['body']['items']['item']['food_Code'])
    print("food_Grupp: " + dict_obj['response']['body']['items']['item']['food_Grupp'])
    print("food_Nm: " + dict_obj['response']['body']['items']['item']['food_Nm'])
    print("food_Eng_Nm: " + dict_obj['response']['body']['items']['item']['food_Eng_Nm'])
    print("origin_Nm: " + dict_obj['response']['body']['items']['item']['origin_Nm'])
    print("examin_Year: " + dict_obj['response']['body']['items']['item']['examin_Year'])
    print("###########################")

    for i in range(0, len(dict_obj['response']['body']['items']['item']['irdnt'])) :
        print()
        print("************************ irdnt_Se_Nm: " + dict_obj['response']['body']['items']['item']['irdnt'][i]['irdnt_Se_Nm'])
        for j in range(0,len(dict_obj['response']['body']['items']['item']['irdnt'][i]['irdnttcket'])):
            print(dict_obj['response']['body']['items']['item']['irdnt'][i]['irdnttcket'][j]['irdnt_Nm'] + ": " +\
                  dict_obj['response']['body']['items']['item']['irdnt'][i]['irdnttcket'][j]['cont_Info'])

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
api_url = "http://apis.data.go.kr/1390802/AgriFood/FdFoodCkryImage"

# read api key
api_key = "api key"

api_uri = f"{api_url}/getKoreanFoodFdFoodCkryImageList"

print(api_uri)

paramDict = {
    'serviceKey': api_key,
    'service_Type': 'xml',
    'Page_No': 1,
    'Page_Size': 1,
    'food_Name': '무',
    'ckry_Name': '국'
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)

# response body
#print(response.text)

dict_obj = xmltodict.parse(response.text)
json_obj = json.dumps(dict_obj)
print(json_obj)

# response body
if dict_obj['response']['header']['result_Code'] == "200":
    print("\nfd_Code: " + dict_obj['response']['body']['items']['item']['fd_Code'])
    print("upper_Fd_Grupp_Nm: " + dict_obj['response']['body']['items']['item']['upper_Fd_Grupp_Nm'])
    print("fd_Nm: " + dict_obj['response']['body']['items']['item']['fd_Nm'])
    print("fd_Wgh: " + dict_obj['response']['body']['items']['item']['fd_Wgh'])
    print("ckry_Nm: " + dict_obj['response']['body']['items']['item']['ckry_Nm'])
    print("ckry_Sumry_Info: " + dict_obj['response']['body']['items']['item']['ckry_Sumry_Info'])
    print("=========================\n")
    print("재료수:" + dict_obj['response']['body']['items']['item']['food_Cnt'])
    print("=========================\n")

    for i in range(0, int(dict_obj['response']['body']['items']['item']['food_Cnt'])):
        print("\n")
        print("food_Code: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['food_Code'])
        print("food_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['food_Nm'])
        print("food_Eng_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['food_Eng_Nm'])
        print("nation_Std_Food_Grupp_Code_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['nation_Std_Food_Grupp_Code_Nm'])
        print("origin_Code_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['origin_Code_Nm'])
        print("food_Wgh: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['food_Wgh'])
        print("allrgy_Info: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['allrgy_Info'])
        print("onslf_Std_Food_Grupp_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['onslf_Std_Food_Grupp_Nm'])
        print("amplt_Cl_Nm: " + dict_obj['response']['body']['items']['item']['food_List']['food'][i]['amplt_Cl_Nm'])
        print("food_Image_Address: " + str(dict_obj['response']['body']['items']['item']['food_List']['food'][i]['food_Image_Address']))


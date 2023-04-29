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
api_url = "http://www.naas.go.kr/unityapi/service/byPass/SoilEnviron/waterPrscrptn"

# read api key
api_key = input("밭작물물관리 API 인증키를 입력하세요: ")

api_uri = f"{api_url}/getWaterPrscrptn"

paramDict = {
    'SG_APIM': api_key,
    'view_Cd': 'WS0095',
    'vapour_Stad_Gbn': '01',
    'mth_Cd': '01',
    'in_House': 100
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict, verify=False)

# response body
#print(response.text)

dict_obj = xmltodict.parse(response.text)
json_obj = json.dumps(dict_obj)
#print(json_obj)

if dict_obj['response']['header']['result_Code'] == "200":
    print(dict_obj['response']['body']['items']['item']['view_Cd'])
    print(dict_obj['response']['body']['items']['item']['sgg_Nm'])
    print(dict_obj['response']['body']['items']['item']['crop_Nm'])
    print(dict_obj['response']['body']['items']['item']['planting_Nm'])
    print(dict_obj['response']['body']['items']['item']['vapour_Stad_Nm'])
    print(dict_obj['response']['body']['items']['item']['mth_Nm'])
    print(dict_obj['response']['body']['items']['item']['in_House'])
    print(dict_obj['response']['body']['items']['item']['growth_Step_Water_Total'])
    print(dict_obj['response']['body']['items']['item']['step_Day_Total'])
    print("======================================")
    for i in range(0, len(dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'])):
        print(dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'][i]['growth_Step_Cnt'])
        print("생육단계:", dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'][i]['step_Nm'])
        print("생육기간:", dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'][i]['step_Day'])
        print("생육기 총관개량:", dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'][i]['growth_Step_Water'])
        print("1일 관개량:", dict_obj['response']['body']['items']['item']['growth_List']['growth_Item'][i]['day_Step_Water'])
        print("------------------------------------")

#################################################


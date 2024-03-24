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
region = 'hadong'
itemsList = ['tmax', 'tmin', 'rain']
daysList = ['20230716', '20230717']
items =','.join(itemsList)
days = ','.join(daysList)
geocode ='127.72743,35.09714'
api_url = f"https://hadong.agmet.kr/farm/pickvalue/{region}/{items}/{days}/{geocode}/json"

print(api_url)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers)

# response body
dict_obj = response.json()

if response.status_code == 200:
    for j in daysList:
        for k in itemsList:
            print(j, k, dict_obj[k][j][geocode], dict_obj[k][j][geocode], dict_obj[k][j][geocode])


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests
import xmltodict
import datetime as dt

# pip install requests

# server URL
region = 'hadong'
daysList = list()
geocode ='127.72743,35.09714'

itemsList = ['tmax', 'tmin', 'rain']
items =','.join(itemsList)

dt_today = dt.datetime.now()
dt_i = dt_today - dt.timedelta(days=3)

for i in range(0, 7):
    date = dt.datetime.strftime(dt_i, "%Y%m%d")
    dt_i = dt_i + dt.timedelta(days=1)
    daysList.append(date)

days = ','.join(daysList)

# request url
api_url = f"https://hadong.agmet.kr/farm/pickvalue/{region}/{items}/{days}/{geocode}/json"
print(api_url)
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url, headers=headers)

# response body
dict_obj = response.json()

if response.status_code == 200:
    for j in daysList:
        print()
        for k in itemsList:
            if dict_obj[k][j] :
                print(j, k, dict_obj[k][j][geocode])


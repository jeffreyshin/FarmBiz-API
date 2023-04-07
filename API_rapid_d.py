# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# server URL
api_url_technell = 'http://147.46.206.95:7890/SNFD'

data = {
  'mPH': 5.4,
  'mEC': 3.6,
  'mNO3': 179,
  'mPO4': 155,
  'mEH': 370,
  'mSO4': 250,
  'mCL': 100,
  'mCROP': "good"
}

payload = data

headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.post(api_url_technell, headers=headers, json=payload)

print(response.text)

# print(response.text)
# print(payload)
# print(headers)





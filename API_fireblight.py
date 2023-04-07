# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import json
import math
import urllib.request
import requests

# server URL
api_url = "http://fireblight.org/fireblight"

# read api key

api_uri = f"{api_url}/getMaryblyt"

paramDict = {
    'begin': '2023-03-27',
    'until': '2023-04-02',
    'plant': 'pear',
    'lon': 126.9,
    'lat': 37.4
}

print(api_uri)

# request url
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_uri, headers=headers, params=paramDict)
print(response.text)

r = response.json()

for i in range(0, 6):
    print(r[i])

# response body



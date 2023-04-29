# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import numpy
import numpy as np
import matplotlib.pyplot as plt


import json
import math
import urllib.request
import requests


# server URL
api_url_greentom2 = 'http://147.46.206.95:7895/greentom2'

#headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'multipart/form-data; charset=utf-8'}
file = {'file': open('greentom2.zip', 'rb')}

#response = requests.post(api_url_greentom2, headers=headers, files=file)
response = requests.post(api_url_greentom2, files=file)

#print(response.status_code)
#print(response.headers)
print(response.text)

with open('greentom2.out', 'w') as file_data:
   file_data.write(response.text)

r = response.json()
output = json.loads(r['output'])

x = list()
y1= list()
y2= list()

for i in range(0, 23):
   y1.append(output[f'{i}']['TDMS'])
   y2.append(output[f'{i}']['Temperature'])
x = range(len(y1))

plt.plot(x, y2)
plt.scatter(x, y1)
plt.title("Scatter Plot of the data")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

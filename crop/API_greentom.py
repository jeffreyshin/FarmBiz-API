# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# _*_ coding: utf-8 _*_

import numpy
import numpy as np
import matplotlib.pyplot as plt
import base64
import time

import json
import math
import urllib.request
import requests
import zipfile
import csv

def fileToBase64(filepath):
   fp = open(filepath, "rb")
   data = fp.read()
   fp.close()
   return base64.b64encode(data).decode("utf-8")


# server URL
urlm = 'https://greentom-api.camp.re.kr/Greentom'

# get Sample
url = f"{urlm}/getSample"
apikey = '61cdc660a46f4fcc93004de201c58dff'
param = {"apiKey": apikey}
res = requests.post(url=url, json=param)

if res.status_code == 200:
    file_path = 'Sample.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# create session
url = f"{urlm}/connect"
apikey = "61cdc660a46f4fcc93004de201c58dff"
param = {"apiKey": apikey}
res = requests.post(url=url, json=param)
jobid = res.content.decode('utf-8')
print(jobid)

# launch model by session key
inputfile = fileToBase64("./Sample.zip")
params = {"apiKey": apikey, "jobid": jobid, "file": inputfile}
url = f"{urlm}/launch"
res = requests.post(url=url, json=params)
r = res.content.decode('utf-8')
print(r)

# get Status model
url = f"{urlm}/getStatus"
params = { "apiKey" : apikey, "jobid": jobid}
res = requests.post(url=url, json=params)
if res.status_code == 200:
    while True:
        res = requests.post(str(url), json=params)
        status = res.content.decode('utf-8')
        if status == "completed":
            print("completed")
            break
        else:
            print("running")
            time.sleep(3)

# get output
url = f"{urlm}/getOutput"
params = { "apiKey" : apikey, "jobid": jobid, "variable" : "all"}
res = requests.post(url=url, json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
url = f"{urlm}/disconnect"
params = { "apiKey" : apikey, "jobid": jobid }
res = requests.post(str(url), json=params)
r = res.content.decode('utf-8')
print(r)

# 해제하기
with zipfile.ZipFile('output.zip') as myzip:
    myzip.extractall()

##############################################################
# import pandas
import pandas as pd
# read csv
data = pd.read_csv('./output_daily.csv')

# Convert the DataFrame to a Dictionary
output = data.to_dict(orient='records')
print(output)

###############################################################
##############################################################

#print(response.status_code)
#print(response.headers)
#print(response.text)

x = list()
y1= list()
y2= list()

for i in range(0, len(output)):
   y1.append(output[i]['TDMS'])
   y2.append(output[i]['Temperature'])
x = range(len(y1))

plt.plot(x, y2)
plt.scatter(x, y1)
plt.title("Scatter Plot of the data")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

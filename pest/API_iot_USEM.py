# pip install requests
import requests

import json
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#################################################

def get_data(dt_now, DELTA):

    custom_dt = ["0"] * DELTA
    datetime = ["0"] * DELTA
    humidity = [0] * DELTA
    temperature = [0] * DELTA
    leafwet = [0] * DELTA
    co2 = [0] * DELTA
    soiltemp = [0] * DELTA
    quantum = [0] * DELTA

    dt_run = dt_now - dt.timedelta(hours=DELTA)
    for i in range(0, DELTA):
        date = dt.datetime.strftime(dt_run, "%Y%m%d")
        time = dt.datetime.strftime(dt_run, "%H")
        #print(i, date, time)
        dt_run = dt_run + dt.timedelta(hours = 1)
        api_uri = f"{api_url_r}/{api_key_r}/{date}/{time}"

# request url
        response = requests.get(api_uri, verify=False)

# response body
        json_obj = json.loads(response.text)

        custom_dt[i] = json_obj['datas'][0]['custom_dt']
        datetime[i] = f"{date} {time}00"
        humidity[i] = json_obj['datas'][0]['humidity']
        temperature[i] = json_obj['datas'][0]['temperature']
        leafwet[i] = json_obj['datas'][0]['leafwet']
        co2[i] = json_obj['datas'][0]['cotwo']
        soiltemp[i] = json_obj['datas'][0]['gtemperature']
        quantum[i] = json_obj['datas'][0]['quantum']

    usem = dict()
    usem['datetime'] = datetime
    usem['temperature'] = temperature
    usem['humidity'] = humidity
    usem['leafwet'] = leafwet
#    usem['soiltemp'] = soiltemp
#    usem['co2'] = co2
#    usem['quantum'] = quantum

    return(usem)

########################################################
DDAY = 1
DELTA = DDAY * 24

# server URL
api_url_r = "http://iot.rda.go.kr/api"
# api key : read access
api_key_r = input("IOT portal 인증키를 입력하세요: ")

dt_now = dt.datetime.now()
date = dt.datetime.strftime(dt_now, "%Y%m%d")
time = dt.datetime.strftime(dt_now, "%H")
DELTA2 = int(time) % 12
#print(DELTA2)

usem = get_data(dt_now, DELTA+DELTA2)

df_usem = pd.DataFrame(usem)

df_usem = df_usem.sort_values("datetime", ascending = True)
print(df_usem)

df_usem.to_csv("./usem.csv", index = False)

# server URL
api_url_anthracnose = 'http://147.46.206.95:7897/Anthracnose'
api_url_botrytis = 'http://147.46.206.95:7898/Botrytis'

headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'multipart/form-data; charset=utf-8'}
file = {'file': open('usem.csv', 'rb')}

response = requests.post(api_url_anthracnose, files=file)

r = response.json()
output = json.loads(r['output'])
#print(json.dumps(output))

x = list()
DATE = list()
PINF = list()
LW = list()
WT = list()

for i in range(0, DDAY+1):
    DATE.append(output[f'{i}']['date'])
    PINF.append(output[f'{i}']['PINF'])
    LW.append(output[f'{i}']['LW'])
    WT.append(output[f'{i}']['WT'])

x = range(len(PINF))

plt.scatter(x, PINF)
#plt.scatter(x, LW)
#plt.plot(x, WT)
plt.title("Scatter Plot of the data")
plt.xlabel("X")
plt.ylabel("PINF")
plt.show()

# pip install requests
import requests

import json
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
import urllib3

import base64
import time

import zipfile

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode("utf-8")

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
        time0 = dt.datetime.strftime(dt_run, "%H")
        # print(i, date, time0)
        dt_run = dt_run + dt.timedelta(hours=1)
        api_uri = f"{api_url_r}/{api_key_r}/{date}/{time0}"
        print(api_uri)

        # request url
        response = requests.get(api_uri, verify=False)
        # print(response.text)
        # response body

        json_obj = json.loads(response.text)

        custom_dt[i] = json_obj['datas'][0]['custom_dt']
        datetime[i] = f"{date} {time0}00"
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

    return (usem)


########################################################
DDAY = 1
DELTA = DDAY * 24

# server URL
api_url_r = "http://iot.rda.go.kr/api"
# api key : read access
api_key_r = input("IOT portal 인증키를 입력하세요: ")

dt_now = dt.datetime.now()
date = dt.datetime.strftime(dt_now, "%Y%m%d")
time0 = dt.datetime.strftime(dt_now, "%H")
DELTA2 = int(time0) % 12
if int(time0) < 12:
    DELTA2 = DELTA2 + 12

print(DELTA2)

usem = get_data(dt_now, DELTA + DELTA2)

df_usem = pd.DataFrame(usem)

df_usem = df_usem.sort_values("datetime", ascending=True)
print(df_usem)

df_usem.to_csv("./weather.csv", index=False)

# server URL
api_url_anthracnose = 'https://anthracnose-api.camp.re.kr/Anthracnose'
api_url_botrytis = 'https://botrytis-api.camp.re.kr/Botrytis'

headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'multipart/form-data; charset=utf-8'}
file = {'file': open('weather.csv', 'rb')}

# 파일 합치기
with zipfile.ZipFile('Sample.zip', 'w') as myzip:
    myzip.write('weather.csv')

urlm = api_url_anthracnose

# get Sample
url = f"{urlm}/getSample"
apikey = '61cdc660a46f4fcc93004de201c58dff'
param = {"apiKey": apikey}
res = requests.post(url=url, json=param)

if res.status_code == 200:
    file_path = 'Sample2.zip'
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
url = 'https://anthracnose-api.camp.re.kr/Anthracnose/launch'
res = requests.post(url=url, json=params)
r = res.content.decode('utf-8')
print(r)

# get Status model
url = 'https://anthracnose-api.camp.re.kr/Anthracnose/getStatus'
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
url = 'https://anthracnose-api.camp.re.kr/Anthracnose/getOutput'
params = { "apiKey" : apikey, "jobid": jobid, "variable" : "all"}
res = requests.post(url=url, json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
url = 'https://anthracnose-api.camp.re.kr/Anthracnose/disconnect'
params = { "apiKey" : apikey, "jobid": jobid }
res = requests.post(str(url), json=params)
r = res.content.decode('utf-8')
print(r)

# 해제하기
with zipfile.ZipFile('output.zip') as myzip:
    myzip.extractall()


# response = requests.post(api_url_anthracnose, files=file)
###############################################################
fp = open("./output.csv", "rb")
response = fp.read()
fp.close()
###############################################################

r = response.json()
output = json.loads(r['output'])
print(json.dumps(output, indent=4, sort_keys=True))
##############################################################3
x = list()
DATE = list()
PINF = list()
LW = list()
WT = list()

for i in range(0, DDAY + 1):
    DATE.append(output[i]['date'])
    PINF.append(output[i]['PINF'])
    LW.append(output[i]['LW'])
    WT.append(output[i]['WT'])

x = range(len(PINF))

plt.scatter(x, PINF)
# plt.scatter(x, LW)
# plt.plot(x, WT)
plt.title("Scatter Plot of the data")
plt.xlabel("X")
plt.ylabel("PINF")
plt.show()

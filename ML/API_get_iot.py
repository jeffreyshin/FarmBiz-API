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
    dt_run = dt.datetime(2023, 5, 1)
    for i in range(0, DELTA):
        date = dt.datetime.strftime(dt_run, "%Y%m%d")
        time = dt.datetime.strftime(dt_run, "%H")
        # print(i, date, time)
        dt_run = dt_run + dt.timedelta(hours=1)
        api_uri = f"{api_url_r}/{api_key_r}/{date}/{time}"
        print(api_uri)

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

    datat = dict()
    datat['datetime'] = datetime
    datat['temperature'] = temperature
    datat['humidity'] = humidity
    datat['leafwet'] = leafwet
    #    usem['soiltemp'] = soiltemp
    #    usem['co2'] = co2
    #    usem['quantum'] = quantum

    return (datat)


########################################################
DDAY = 20
DELTA = DDAY * 24

# server URL
api_url_r = "http://iot.rda.go.kr/api"
# api key : read access
api_key_r = input("IOT portal 인증키를 입력하세요: ")

dt_now = dt.datetime.now()
date = dt.datetime.strftime(dt_now, "%Y%m%d")
time = dt.datetime.strftime(dt_now, "%H")


data = get_data(dt_now, DELTA)

df_data = pd.DataFrame(data)

df_data = df_data.sort_values("datetime", ascending=True)
print(df_data)

df_data.to_csv("./data.csv", index=False)

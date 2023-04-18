# pip install requests
import requests

import json
import datetime as dt
import pandas as pd

DELTA = 2 * 24

custom_dt = ["x" for i in range(DELTA)]
datetime = ["x" for i in range(DELTA)]
humidity = [0 for i in range(DELTA)]
temperature = [0 for i in range(DELTA)]
leafwet = [0 for i in range(DELTA)]
co2 = [0 for i in range(DELTA)]
soiltemp = [0 for i in range(DELTA)]
quantum = [0 for i in range(DELTA)]

# server URL
api_url_r = "http://iot.rda.go.kr/api"
# api key : read access
api_key_r = "API_KEY"

#################################################

def get_data(dt_now, DELTA):
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
        datetime[i] = json_obj['datas'][0]['datetime']
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
    usem['soiltemp'] = soiltemp
    usem['co2'] = co2
    usem['quantum'] = quantum
    print(temperature)

    return(usem)

########################################################

dt_now = dt.datetime.now()
usem = get_data(dt_now, DELTA)

df_usem = pd.DataFrame(usem)
#print(df_usem.sort_values("datetime", ascending = True))
print(df_usem)

with open('usem.txt', 'w') as file_data:
   file_data.write(str(df_usem.sort_values("datetime", ascending = True)))
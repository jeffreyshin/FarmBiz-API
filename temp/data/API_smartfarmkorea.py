# pip install requests
import pandas as pd
import requests

import json

import datetime as dt

# server URL
serviceKey = "API KEY"

# data logging date and time

api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getIdentityDataList"
api_uri = f"{api_url}/{serviceKey}"

print(api_uri)

# request url
response = requests.get(api_uri, verify=False)

# response body
#print(response.text)

json_obj = json.loads(response.text)

# response body
#print(json_obj)

api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getCroppingSeasonDataList"

for i in range(0, 1):
    userid = json_obj[i]['userId']
    fcltyId =json_obj[i]['fcltyId']

api_uri = f"{api_url}/{serviceKey}/{fcltyId}/{userid}"
response = requests.get(api_uri, verify=False)
#print(response.text)

measDate = "20230414"
api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getEnvDataList"
api_uri = f"{api_url}/{serviceKey}/{fcltyId}/{measDate}"
response = requests.get(api_uri, verify=False)

#print(response.text)

json_obj = json.loads(response.text)

dt_now = dt.datetime.strptime(json_obj[0]['measDate'], "%Y-%m-%d %H:%M:%S")

TI = list()
for i in range(0, len(json_obj)) :
    d = dict()
    if json_obj[i]['fatrCode'] == "TI" :
        d['measDate'] = json_obj[i]['measDate']
        d['TI'] = float(json_obj[i]['senVal'])
        TI.append(d)

HI02 = list()
for i in range(0, len(json_obj)) :
    d = dict()
    if json_obj[i]['fatrCode'] == "HI02" :
        d['measDate'] = json_obj[i]['measDate']
        d['HI02'] = float(json_obj[i]['senVal'])
        HI02.append(d)

CI = list()
for i in range(0, len(json_obj)) :
    d = dict()
    if json_obj[i]['fatrCode'] == "CI" :
        d['measDate'] = json_obj[i]['measDate']
        d['CI'] = float(json_obj[i]['senVal'])
        CI.append(d)

SR = list()
for i in range(0, len(json_obj)) :
    d = dict()
    if json_obj[i]['fatrCode'] == "SR" :
        d['measDate'] = json_obj[i]['measDate']
        d['SR'] = float(json_obj[i]['senVal'])
        SR.append(d)

TI_1 = list()
TI_2 = list()
for i in range(0, len(TI)):
    TI_1.append(TI[i]['measDate'])
    TI_2.append(TI[i]['TI'])

TI_3 = dict()
TI_3['measDate'] = TI_1
TI_3['TI'] = TI_2

HI02_1 = list()
HI02_2 = list()
for i in range(0, len(HI02)):
    HI02_1.append(HI02[i]['measDate'])
    HI02_2.append(HI02[i]['HI02'])

HI02_3 = dict()
HI02_3['measDate'] = HI02_1
HI02_3['HI02'] = HI02_2

CI_1 = list()
CI_2 = list()
for i in range(0, len(CI)):
    CI_1.append(CI[i]['measDate'])
    CI_2.append(CI[i]['CI'])

CI_3 = dict()
CI_3['measDate'] = CI_1
CI_3['CI'] = CI_2

df_TI = pd.DataFrame(TI_3, index = TI_3['measDate'])
df_HI02 = pd.DataFrame(HI02_3, index = HI02_3['measDate'])
df_CI = pd.DataFrame(CI_3, index = CI_3['measDate'])

df_M = pd.merge(df_TI, df_HI02, how = 'outer')
df_M = pd.merge(df_M, df_CI, how = 'outer')
print(df_M)


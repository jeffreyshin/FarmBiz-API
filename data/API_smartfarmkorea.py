# pip install requests
import pandas as pd
import requests
import json
import datetime as dt



# server URL
serviceKey = input("datamart_스마트팜혁신밸리 : 인증키를 입력하세요: ")

#########################################
# 농가ID정보
#########################################

api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getIdentityDataList"
api_uri = f"{api_url}/{serviceKey}"
print(api_uri)

# request url
response = requests.get(api_uri, verify=False)

# response body
#print(response.text)

json_obj = json.loads(response.text)

# response body
#print(len(json_obj))

#########################################
# 작기정보
#########################################

api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getCroppingSeasonDataList"

userId = [0]*100
fcltyId = [0]*100

for i in range(0, len(json_obj)):
    userId[i] = json_obj[i]['userId']
    fcltyId[i] =json_obj[i]['fcltyId']

userId_m = "GJ_0000026"
fcltyId_m = "C010902_02_04"

print(userId_m)   #김기형 농가
print(fcltyId_m)

#print(userId[23])   #김기형 농가
#print(fcltyId[23])

api_uri = f"{api_url}/{serviceKey}/{fcltyId_m}/{userId_m}"
response = requests.get(api_uri, verify=False)
print()
r = response.json()
print('##########################################')
print("김기형 농가 작기정보:\n", json.dumps(r,indent = 4, sort_keys = True))
print('##########################################')


#########################################
# 환경정보 항목별 데이터 추출
#########################################

def addValue():
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
    return df_M

#########################################
# 환경정보 조회
#########################################

#dt_now = dt.datetime.now()
#endDate = dt.datetime.strftime(dt_now, "%Y%m%d")
startDt = input("조회 시작일을 입력하세요(yyyyMMdd): ")
endDt = input("조회 종료일을 입력하세요(yyyyMMdd): ")

startDate = dt.datetime.strptime(startDt, "%Y%m%d")
endDate = dt.datetime.strptime(endDt, "%Y%m%d")

df_MM = pd.DataFrame(columns = ['measDate', 'TI', 'HI02', 'CI'])
date_diff = endDate - startDate
dt_now = startDate
api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getEnvDataList"

for i in range(0, date_diff.days):
    measDate = dt_now.strftime("%Y%m%d")
    api_uri = f"{api_url}/{serviceKey}/{fcltyId_m}/{measDate}"
    response = requests.get(api_uri, verify=False)
    json_obj = response.json()
#    print(json.dumps(json_obj, indent=4, sort_keys=True))

    dt_now = dt_now + dt.timedelta(days=1)
    df_M = addValue()
    df_MM = pd.concat([df_MM, df_M])

print(df_MM)
df_MM.to_csv("./smartfarmKorea.csv", index = False)

#    dt_now = dt.datetime.strptime(json_obj[0]['measDate'], "%Y-%m-%d %H:%M:%S")

##########################################
# 생육정보 조회: 해당농가의 생육조사 일련번호(crpsnSn)가 뭔지 알 수 없음
##########################################
api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getExaminDataList"
crpsnSn = 1
api_uri = f"{api_url}/{serviceKey}/{crpsnSn}"
response = requests.get(api_uri, verify=False)
json_obj = response.json()
print(json.dumps(json_obj, indent=4, sort_keys=True))


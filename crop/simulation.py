# pip install requests
import requests
import json

# server URL
api_base_url = "https://core-api.farmdure.notesquare.co.kr/v1"
api_uri = f"{api_base_url}/simulation"
print(api_uri)

data = {
    'crop_key': 'springCabbage',
    'start_doy': 50,

    # NOTICE: parameters 를 json 포맷으로 직렬화한 string 으로 변환
    'parameters': json.dumps([
        {'type': 'harvest', 'name': '수확', 'value': [601, 550], 'ranged': True, 'text': ''},
        {'type': 'base_temperature', 'value': 10},
        {'type': 'gdd_method', 'value': 'm3'}
    ]),
    'weather_data_type': 'csv',
    'weather_start_year': 2005,
    'weather_end_year': 2010,
}
files = {'weather_data': open('Data.csv', 'rb')}

# request url
# NOTICE: Content-Type 을 headers 에서 제거 (requests library 에서 자동으로 생성함)
headers = {'Accept': 'application/json; charset=utf-8'}
response = requests.post(api_uri, headers=headers, files=files, data=data)

# response body
dict_obj = response.json()
print(dict_obj)

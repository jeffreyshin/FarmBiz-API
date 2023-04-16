# pip install requests
import requests

import json

'''
api uri
/api/{read_api_key}/{date}/{hour}

success response
{
    "datas":
        [
            {"dt":"2019-11-21 13:41:55","dry_bulb_tp":"25","wet_bulb_tp":"15","solrad_qy":"20"},
            {"dt":"2019-11-21 13:42:13","dry_bulb_tp":"25","wet_bulb_tp":"15","solrad_qy":"20"},
            ...
        ],
    "resultCode":"",
    "resultMessage":""
}
'''

# iot server URL
api_url_w = "http://iot.rda.go.kr:12345/colct/api/registData.do"
# api key: write access
# api_key_w ="API KEY"

# key=iot_keyvalue&column1=value1&column22=value2...
query_string = f"?key={api_key_w}"
paramDict = {
    'key': api_key_w,
    'id': '3',
    'datetime': '2023-03-24 15:00:00',
    'ph': 6.5,
    'ec': 1.4,
    'no3': 240,
    'po4': 34,
    'eh': 48,
    'k': 1.3,
    'crop': 20
}

# request url?queryString
headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
response = requests.get(api_url_w, headers=headers, params=paramDict)

# response body
print(response.text)

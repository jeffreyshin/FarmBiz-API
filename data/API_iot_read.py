# pip install requests
import requests

import json

'''
api uri
/api/{read_api_key}/{date}/{hour}
/api/w4460bcc0494f41f6a3af01e54bd80c13/20191121/13

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

# server URL
api_url_r = "http://iot.rda.go.kr/api"
# api key : read access
api_key_r = "API KEY"

# data logging date and time
date ="20230308"
time = "12"

api_uri = f"{api_url_r}/{api_key_r}/{date}/{time}"
print(api_uri)

# request url
response = requests.get(api_uri, verify=False)

# response body
print(response.text)
json_obj = json.loads(response.text)

# response body
#print(json_obj)

print("\ncustom_dt: " + json_obj['datas'][0]['custom_dt'])
print("datetime: " + json_obj['datas'][0]['datetime'])
print("ph: " + json_obj['datas'][0]['ph'])
print("ec: " + json_obj['datas'][0]['ec'])
print("eh: " + json_obj['datas'][0]['eh'])
print("no3: " + json_obj['datas'][0]['no3'])
print("po4: " + json_obj['datas'][0]['po4'])


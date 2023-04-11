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

serviceKey = "6f9dcd925fa44a949179d2ea967599e8"

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

for i in range(0, 56):
    userid = json_obj[i]['userId']
    fcltyId =json_obj[i]['fcltyId']
    print(userid, " ", fcltyId)
    api_uri = f"{api_url}/{serviceKey}/{fcltyId}/{userid}"
    response = requests.get(api_uri, verify=False)
    print(response.text)

measDate = "20220703"
api_url = "http://www.smartfarmkorea.net/Agree_WS/webservices/InnovationValleyRestService/getEnvDataList"
api_uri = f"{api_url}/{serviceKey}/{fcltyId}/{measDate}"
response = requests.get(api_uri, verify=False)
print(response.text)



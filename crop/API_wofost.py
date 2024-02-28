import requests
import base64
import time

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode("utf-8")

# get Sample
url = 'https://wofost-api.camp.re.kr/Wofost/getSample'
apikey = '61cdc660a46f4fcc93004de201c58dff'
param = {"apiKey": apikey}
res = requests.post(url=url, json=param)

if res.status_code == 200:
    file_path = 'Sample.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# create session
url = 'https://wofost-api.camp.re.kr/Wofost/connect'
apikey = "61cdc660a46f4fcc93004de201c58dff"
param = {"apiKey": apikey}
res = requests.post(url=url, json=param)
jobid = res.content.decode('utf-8')
print(jobid)


# launch model by session key
inputfile = fileToBase64("./Sample.zip")
params = {"apiKey": apikey, "jobid": jobid, "file": inputfile}
url = 'https://wofost-api.camp.re.kr/Wofost/launch'
res = requests.post(url=url, json=params)
r = res.content.decode('utf-8')
print(r)


# get Status model
url = 'https://wofost-api.camp.re.kr/Wofost/getStatus'
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
url = 'https://wofost-api.camp.re.kr/Wofost/getOutput'
params = { "apiKey" : apikey, "jobid": jobid, "variable" : "all"}
res = requests.post(url=url, json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
url = 'https://wofost-api.camp.re.kr/Wofost/disconnect'
params = { "apiKey" : apikey, "jobid": jobid }
res = requests.post(str(url), json=params)
r = res.content.decode('utf-8')
print(r)

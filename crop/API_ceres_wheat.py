import requests
import base64
import time

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode("utf-8")

urlm = 'https://ceres-wheat-api.camp.re.kr/CeresWheat'
# get Sample
url = f"{urlm}/getSample"
apikey = '61cdc660a46f4fcc93004de201c58dff'
param = { "apiKey" : apikey}
res = requests.post(url=url, json=param)

if res.status_code == 200:
    file_path = 'Sample.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# create session
url = f"{urlm}//connect"
apikey = "61cdc660a46f4fcc93004de201c58dff"
param = { "apiKey" : apikey}
res = requests.post(url=url, json=param)
jobid = res.content.decode('utf-8')
print(jobid)

# launch model by session key
inputfile = fileToBase64("./Sample.zip")
params = { "apiKey" : apikey , "jobid": jobid, "file" : inputfile}
url = f"{urlm}/launch"
res = requests.post(url=url, json=params)
r = res.content.decode('utf-8')
print(r)

# get Status model
url = 'https://ceres-wheat-api.camp.re.kr/CeresWheat/getStatus'
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
url = f"{urlm}/getOutput"
params = { "apiKey" : apikey, "jobid": jobid, "variable" : "ADOY"}
res = requests.post(url=url, json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
url = f"{urlm}/disconnect"
params = { "apiKey" : apikey, "jobid": jobid }
res = requests.post(str(url), json=params)
r = res.content.decode('utf-8')
print(r)

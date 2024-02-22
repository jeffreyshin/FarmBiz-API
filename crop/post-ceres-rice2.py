import requests
import base64
import time

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode("utf-8")

apikey = '61cdc660a46f4fcc93004de201c58dff'
jobid = '6df15d6dd614225cc6ada1ca3d832e95'
# get Sample
#url = 'http://192.168.0.9:8085/CeresRice/getSample'
#res = requests.post(str(url))

#if res.status_code == 200:
#    file_path = 'Sample.zip'
#    with open(file_path, 'wb') as file:
#        file.write(res.content)

# create session
#params = { "apiKey" : apikey }
#url = 'http://192.168.0.9:8085/CeresRice/connect'
#res = requests.post(str(url), json=params)
#jobid = res.content.decode('utf-8')
#print(jobid)
#
#
## launch model by session jobid
#inputfile = fileToBase64("./Sample.zip")
#params = { "apiKey" : apikey, "jobid" : jobid , "file" : inputfile}
#url = 'http://192.168.0.9:8085/CeresRice/launch'
#res = requests.post(str(url), json=params)
#rescon = res.content.decode('utf-8')
#print(rescon)
#
## get Status model
#url = 'http://192.168.0.9:8085/CeresRice/getStatus'
#params = { "apiKey" : apikey, "jobid" : jobid }
#res = requests.post(str(url), json=params)
#if res.status_code == 200:
#    while True:
#        res = requests.post(str(url), json=params)
#        status = res.content.decode('utf-8')
#        if status == "completed":
#            print("completed")
#            break
#        else:
#            print("running")
#            time.sleep(3)

# get output
url = 'https://ceres-rice-api.camp.re.kr/CeresRice/getOutput'
params = { "apiKey" : apikey, "jobid" : jobid, "variable" : "all"}
res = requests.post(str(url), json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
#url = 'http://192.168.0.9:8085/CeresRice/disconnect'
#params = { "apiKey" : apikey, "jobid" : jobid }
#res = requests.post(str(url), json=params)
#jobid = res.content.decode('utf-8')
#print(jobid)

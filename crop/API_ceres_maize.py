import requests
import base64
import time

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
    return base64.b64encode(data).decode("utf-8")

# get Sample
url = 'http://192.168.0.9:8085/CeresMaize/getSample'
res = requests.post(str(url))

if res.status_code == 200:
    file_path = 'Sample.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# create session
url = 'http://192.168.0.9:8085/CeresMaize/connect'
res = requests.post(str(url))
key = res.content.decode('utf-8')
print(key)


# launch model by session key
inputfile = fileToBase64("./Sample.zip")
params = { "key" : key , "file" : inputfile}
url = 'http://192.168.0.9:8085/CeresMaize/launch'
res = requests.post(str(url), json=params)
rescon = res.content.decode('utf-8')
print(rescon)

# get Status model
url = 'http://192.168.0.9:8085/CeresMaize/getStatus'
params = { "key" : key }
res = requests.post(str(url), json=params)
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
url = 'http://192.168.0.9:8085/CeresMaize/getOutput'
params = { "key" : key }
res = requests.post(str(url), json=params)
if res.status_code == 200:
    file_path = 'output.zip'
    with open(file_path, 'wb') as file:
        file.write(res.content)

# remove session
url = 'http://192.168.0.9:8085/CeresMaize/disconnect'
params = { "key" : key }
res = requests.post(str(url), json=params)
key = res.content.decode('utf-8')
print(key)

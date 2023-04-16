# pip install pandas

import pandas as pd
import json
import requests

import zipfile

with open('a.txt', 'w') as file_data:
   file_data.write("file a.txt")

with open('b.txt', 'w') as file_data:
   file_data.write("file b.txt")

with open('c.txt', 'w') as file_data:
   file_data.write("file c.txt")

# 파일 합치기
with zipfile.ZipFile('mytext.zip', 'w') as myzip:
    myzip.write('a.txt')
    myzip.write('b.txt')
    myzip.write('c.txt')

# 해제하기
with zipfile.ZipFile('mytext.zip') as myzip:
    myzip.extractall()


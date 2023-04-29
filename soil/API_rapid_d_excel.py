# pip install pandas

import pandas as pd
import json
import requests

api_url_technell = 'http://147.46.206.95:7890/SNFD'

print("start---------------------")
from datetime import datetime as dt

# pandas
df_excel = pd.read_excel("rapid_d.xlsx",sheet_name="rapid_d", engine="openpyxl", index_col="ID")
# print(df_excel)

for i in range(0, 10):
    # measurements = df_excel.iloc[i, 0:7]
    data = {
        'mPH': float(df_excel.iloc[i, 0]),
        'mEC': float(df_excel.iloc[i, 1]),
        'mNO3': int(df_excel.iloc[i, 2]),
        'mPO4': int(df_excel.iloc[i, 3]),
        'mK': int(df_excel.iloc[i, 4]),
        'mEH': int(df_excel.iloc[i, 5]),
        'mCROP': int(df_excel.iloc[i, 6])
    }
    print(data)
    payload = data
    headers = {'Accept': 'application/json; charset=utf-8', 'Content-Type': 'application/json; charset=utf-8'}
    response = requests.post(api_url_technell, headers=headers, json=payload)
    print(response.text)

# pip install pandas

import pandas as pd
import json
import requests

from geopy.geocoders import Nominatim

geolocoder = Nominatim(user_agent = 'South Korea')

def geocoding(address):
    geo = geolocoder.geocode(address)
    crd = (geo.latitude, geo.longitude)
    print(crd)
    return crd

print("start---------------------")

tags = {'amenity': True}

address_list = ['오공로 70',
'농생명로 300',
'현충로 213']

for i in address_list:
    print(i)
    crd = geocoding(i)


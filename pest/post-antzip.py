import requests
import base64
import zipfile

def fileToBase64(filepath):
    fp = open(filepath, "rb")
    data = fp.read()
    fp.close()
#    return base64.b64encode(data)
    return base64.b64encode(data).decode("ascii")

with zipfile.ZipFile('./input.zip', 'w', compression=zipfile.ZIP_DEFLATED) as input_zip:
    f = open("./weather.csv", "r")
    inputfile = f.read()
    input_zip.writestr( 'weather.csv', str(inputfile))
    f.close()
#
new_zip = fileToBase64("./input.zip")

# print(new_zip)
new_zip2 = "UEsDBBQAAAgIAA+qyVaFo0+DAAIAAF8GAAALAAAAd2VhdGhlci5jc3ZllV2KWzEMhd8L3cMsQBhb8o+0nMDc0kADZbhD6e4rWTcZy4U8hHzIko+OT95v53HeHwecx+P38XE7Pz8O+Pn5uL/fz7/w67j9+HOc379hRsq1jLeCOQOW1KFSYsgrIkcCFVOJqBpCoJ4G5NRX1AyRVqEkilXdEQFpTUTDew0g3BErKmJj9H0MMdSh51QD0EspIP2183YcFkcEw3gcHtFhgVET7tD0KDbjaKkpHC/Ib3l2RBhsM0Y0O6LVDZM4wq+OrFfc4OxIwDiHkRVVr0PgMncQYHOoHfM8tK/QtlCaaSNTgNBxOJTnOLxCdrl5rih29E1oRx2nbHUl+6EK2TacaIVTnaq/S1FV64rwWacIoYRJpzu1I4FkrSvhjtOfWokgJh2GWadDpwBiKAzT/YZaVXd0KUM2DEOL/dhh834tlRWK31CPtX3pt1Uct2pV0cREKG1lrg1I046R4Kuq68GR0dNS0uOJctmUbNBhqgV2vYxujDeGT0fJTuj5nsSsH5mb1AhupPlbmqxurPt7acb6xsZLS5uxL1uQy59iPrMblhWJo/J8g7zA6U+0lfeyPRdxf6L5rI4tEuRKTzZI/0NThiyaat6SRq4EtVQjCbkr7k/SD4f8lCs/7RKahBLR8CnRspD3XqYLWqB1T6cAxZO3AltWBLWnNzFbyNifgz6Hf1BLAQIUABQAAAgIAA+qyVaFo0+DAAIAAF8GAAALAAAAAAAAAAAAAAC2gQAAAAB3ZWF0aGVyLmNzdlBLBQYAAAAAAQABADkAAAApAgAAAAA="
params = { "Input" : new_zip2, "type" : "file"}
paramss = {"Input":"UEsDBBQAAAgIAA+qyVaFo0+DAAIAAF8GAAALAAAAd2VhdGhlci5jc3ZllV2KWzEMhd8L3cMsQBhb8o+0nMDc0kADZbhD6e4rWTcZy4U8hHzIko+OT95v53HeHwecx+P38XE7Pz8O+Pn5uL/fz7/w67j9+HOc379hRsq1jLeCOQOW1KFSYsgrIkcCFVOJqBpCoJ4G5NRX1AyRVqEkilXdEQFpTUTDew0g3BErKmJj9H0MMdSh51QD0EspIP2183YcFkcEw3gcHtFhgVET7tD0KDbjaKkpHC/Ib3l2RBhsM0Y0O6LVDZM4wq+OrFfc4OxIwDiHkRVVr0PgMncQYHOoHfM8tK/QtlCaaSNTgNBxOJTnOLxCdrl5rih29E1oRx2nbHUl+6EK2TacaIVTnaq/S1FV64rwWacIoYRJpzu1I4FkrSvhjtOfWokgJh2GWadDpwBiKAzT/YZaVXd0KUM2DEOL/dhh834tlRWK31CPtX3pt1Uct2pV0cREKG1lrg1I046R4Kuq68GR0dNS0uOJctmUbNBhqgV2vYxujDeGT0fJTuj5nsSsH5mb1AhupPlbmqxurPt7acb6xsZLS5uxL1uQy59iPrMblhWJo/J8g7zA6U+0lfeyPRdxf6L5rI4tEuRKTzZI/0NThiyaat6SRq4EtVQjCbkr7k/SD4f8lCs/7RKahBLR8CnRspD3XqYLWqB1T6cAxZO3AltWBLWnNzFbyNifgz6Hf1BLAQIUABQAAAgIAA+qyVaFo0+DAAIAAF8GAAALAAAAAAAAAAAAAAC2gQAAAAB3ZWF0aGVyLmNzdlBLBQYAAAAAAQABADkAAAApAgAAAAA=","type":"file"}
url = 'http://147.46.206.95:7897/Anthracnose'
print(params)
res = requests.post(str(url), json=paramss)
content = res.content.decode('ascii')
print(content)

import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import linear_model
from sklearn.model_selection import train_test_split

import glob

stn_number = "114"
dir_path = "."   #dataset/ASOS/" + stn_number
filename = glob.glob(dir_path + "/data_gongju.csv")
# df = pd.read_csv(filename[0], encoding="cp949")
df = pd.read_csv("./data_gonju.csv", encoding="cp949")

df.columns = ["stn_no","stn_name","date","temperature","WS","RI","pressure", "humidity", "itemp", "ihumidity", "leafwet"]
df = df.drop(columns=["stn_no","stn_name","WS","RI", "pressure", "ihumidity", "leafwet"])

print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())

# 데이터를 tensor로 변경
X_train = torch.Tensor([[x] for x in list(df.temperature)])
x2_train = torch.Tensor([[x] for x in list(df.humidity)])
y_train = torch.torch.FloatTensor([[x] for x in list(df.itemp)])

# TensorDataset으로 변경
train_data = TensorDataset(X_train, y_train)

# 배치사이즈를 설정하고 Dataloader 세팅
batch_size = len(X_train)
train_dl = DataLoader(train_data, batch_size, shuffle=True)

# 임의의 모델 설정
model = net = torch.nn.Sequential(
    torch.nn.Linear(1, 250),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(250, 125),
    torch.nn.LeakyReLU(),
    torch.nn.Linear(125, 1),
)

# 비용함수 설정 : MSE
loss_fn = torch.nn.MSELoss()

# 활성화함수 설정 : Adam
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

num_epochs = 200

for epoch in range(num_epochs):
    for step, (xb, yb) in enumerate(train_dl):
        pred = model(xb)
        loss = loss_fn(pred, yb)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))

print(pred)



# sns.jointplot(x=df["itemp"], y=df["temperature"])

plt.plot(df["date"], df["temperature"], 'ro', label='target')
plt.plot(df["date"], df["itemp"], 'bo', label='target')

plt.show()

#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Import Librarys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pylab as pl
import sklearn
from sklearn.metrics import accuracy_score
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# get_ipython().run_line_magic('matplotlib', 'inline')

#You can download it from https://open.canada.ca/data/en/dataset/98f1a129-f628-4ce4-b24d-6f16bf24dd64. 
#I have downloaded and copied in my PC

url = "MY2019_Fuel_Consumption_Ratings.csv"
#url.encode('utf-8').strip()

dataset = pd.read_csv(url,encoding = 'unicode_escape',skiprows = [1]) # skip second row of unit description

# take a look at the dataset
#dataset.head()
#feature extraction

features = dataset[['Engine Size','Cylinders','Fuel Consumption','CO2 Emissions']]

# change the header names
features.columns = ['Engine_Size', 'Cylinders','Fuel_Consumption','CO2_Emissions']

#features.head(20)
# drop the nan based rows

features = features.dropna() 

# plt.scatter(features.Engine_Size, features.CO2_Emissions, color='blue')
# plt.xlabel("Engine_Size")
# plt.ylabel("Emission")
# plt.show()

# splitting data for multiple linear regression
X = features[['Engine_Size','Cylinders','Fuel_Consumption']]
y = features[['CO2_Emissions']]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=21)

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X_train, y_train)
# make the prediction using X-test

# make the prediction
y_pred = regr.predict(X_test)

# The Reg coefficients
print('Coefficients: \n', regr.coef_)

# The mean squared error
print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))

# The coefficient of determination
print('Coefficient of determination: %.2f' % r2_score(y_test, y_pred))

# Plot outputs
plt.scatter(X_test.Engine_Size, y_test,  color='black')

plt.plot(X_test.Engine_Size, y_pred, color='blue')
plt.xticks(())
plt.yticks(())

plt.show()

#testing the model

#print (y_test)
print(accuracy_score(y_pred,y_test))






# In[ ]:





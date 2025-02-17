# Program:48
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Create a Homeprice data set in csv file. Write a program to find out the prediction 
# model for the Homeprice, where the price will be calculated based on area. Use the Linear Regression model.
# Date: 2.11.2024

import pandas as pd 
from sklearn import linear_model
import numpy as np

df=pd.read_csv("C:/Users/homeprice.csv")
print(df)

model=linear_model.LinearRegression()
model

model.fit(df[['rice','daal','fish','chicken']], df.Price)
model.predict([[300,50,2,2]]))#put the values

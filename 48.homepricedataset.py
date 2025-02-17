# Program:48
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: Create a Homeprice data set in csv file. Write a program to find out the prediction 
# model for the Homeprice, where the price will be calculated based on area. Use the Linear Regression model.
# Date: 2.11.2024

import pandas as pd 
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/Tanisha/homeprice.csv")
print(df)

plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.Area, df.Price, color="Red", marker="*")
plt.show()

new_df=df.drop('Price', axis='columns')
print(new_df)

model=linear_model.LinearRegression()
print(model)

model.fit(new_df, df.Price)#model is getting trained
print("the value from graph is: ")
print(model.predict([[1400]]))#dataframe=2D array

#to check my prediction is correct or not
print("the value from formula is: ")
m=model.coef_#suppos its m
C= model.intercept_#suppose its C
y=m*(1400)+C 
print(y)
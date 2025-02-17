# Program:50
# Name: Tanisha Seal
# Roll number: 27632423030
# Topic: 
# Consider the dataset of home price
# Area RoomNo  Age	Price
# 1000	2	    6	20000
# 1200	4	    10	21000
# 1250	3	    5	25000
# 1300	2	    15	16000
# 1400	4	    Na	30000
# 1450	2	    10	22000
# 1600	Na	    5	27000
# 1710	3	    12	21000
			
# 1.	Remove Na from the given dataset
# 2.	Find the home price while room no. and age are 4 and below 8 respectively



# Date: 2.11.2024

import pandas as pd 
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("C:/Users/Tanisha/homeprice2.csv")
print(df)

df = df.replace('Na', pd.NA)
df_cleaned = df.dropna()

#filtered_homes = df_cleaned[(df_cleaned['Room No'] == 4) & (df_cleaned['Age'] < 8)]

filtered_homes = df[(df['Room No'] == 4) & (df['Age'] < 8)]
print(filtered_homes)

# plt.xlabel('Area')
# plt.ylabel('Price')
# plt.scatter(df.Area, df.Price, color="Red", marker="*")
# plt.show()

# new_df=df.drop('Price', axis='columns')
# print(new_df)

# model=linear_model.LinearRegression()
# print(model)

# model.fit(new_df, df.Price)#model is getting trained
# print("the value from graph is: ")
# print(model.predict([[1400]]))#dataframe=2D array

# #to check my prediction is correct or not
# print("the value from formula is: ")
# m=model.coef_#suppos its m
# C= model.intercept_#suppose its C
# y=m*(1400)+C 
# print(y)
import pandas as pd 
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import math

df=pd.read_csv("C:/Users/TANISHA/new_homeprice.csv")#path location slash is diff from the one in python
print(df)

new_bedrooms=math.floor(df.bedrooms.median())

df.bedrooms=df.bedrooms.fillna(new_bedrooms)
print(df)

model=linear_model.LinearRegression()

model.fit(df[['area','bedrooms','age']],df.price)

new_data = pd.DataFrame({'area': [2200], 'bedrooms': [5], 'age': [10]}) 
prediction = model.predict(new_data) 
print(prediction)
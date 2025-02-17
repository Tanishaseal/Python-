import pandas as pd
from sklearn import linear_model
import numpy as np
import math

# Read data from CSV file
df = pd.read_csv("C:/Users/TANISHA/Bedsheet.csv")
print("Original DataFrame:\n", df)

# Fill missing values with median for Width and Thickness
new_width = math.floor(df.Width.median())
df.Width = df.Width.fillna(new_width)
new_thickness = math.floor(df.Thickness.median())
df.Thickness = df.Thickness.fillna(new_thickness)
print("\nDataFrame after filling missing values:\n", df)

# One-hot encode the 'Company' column
df = pd.get_dummies(df, columns=['Company'], drop_first=True)

# Define features and target variable
X = df.drop('Price', axis=1)
y = df['Price']

# Initialize and train the Linear Regression model
model = linear_model.LinearRegression()
model.fit(X, y)

# Verify columns in the training data
print("\nColumns in training data:", X.columns)

# Prepare the input data for prediction
new_data = pd.DataFrame({
    'Length': [300],
    'Width': [240],
    'Thickness': [3],
    'Set': [3],
    'Company_Carlon': [0],
    'Company_Raju': [0],
    'Company_Smriti': [1]
})

# Ensure new_data has the same columns as X
missing_cols = set(X.columns) - set(new_data.columns)
for col in missing_cols:
    new_data[col] = 0

new_data = new_data[X.columns]

# Verify columns in the prediction data
print("\nColumns in prediction data:", new_data.columns)

# Predict the price
predicted_price = model.predict(new_data)
print(f"\nThe predicted price is: {predicted_price[0]}")

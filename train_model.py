# train_model.py

import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import joblib
import json
import os

new_directory_path = "C:/Users/ahmad/OneDrive/Desktop/Deployment Project Portfolio/ebook-revenue-api/"  # Replace with your desired path
os.chdir(new_directory_path)

print("--- Starting Model Training ---")

# 1. Load and Prepare Data
# Make sure the 'Dataset.xlsx' is accessible from where you run this script.
# For simplicity, you can place it in the same 'ebook-revenue-api' folder.
try:
    Dataset = pd.read_excel('Dataset.xlsx', sheet_name='Sheet1')
except FileNotFoundError:
    print("Error: 'Dataset.xlsx' not found. Make sure it's in the correct directory.")
    exit()


Data = Dataset[['Est. Sales', 'Sales Rank', 'Reviews', 'Price_USD', 'Sales_Rev_USD', 'Final_Master_Genre', 'Detected_Language', 'Country']].rename(
    columns={
        'Est. Sales': 'Sales_num',
        'Sales Rank': 'Sales_rank',
        'Price_USD': 'Price',
        'Sales_Rev_USD': 'Sales_rev',
        'Final_Master_Genre': 'Genre',
        'Detected_Language': 'Language'
    }
)

# Handle potential missing values just in case
Data.dropna(inplace=True)

# 2. Feature Engineering (One-Hot Encoding)
# Using get_dummies is simpler for deployment than OneHotEncoder
Data_encoded = pd.get_dummies(Data, columns=['Genre', 'Language', 'Country'], drop_first=True)

# 3. Define Features (X) and Target (y)
features = ['Sales_num', 'Sales_rank', 'Reviews', 'Price'] + \
           [col for col in Data_encoded.columns if col.startswith(('Genre_', 'Language_', 'Country_'))]

X = Data_encoded[features]
y = Data_encoded['Sales_rev']

# Save the column list for the API
model_columns = list(X.columns)
with open('model/model_columns.json', 'w') as f:
    json.dump(model_columns, f)
print("Model columns saved to model/model_columns.json")


# 4. Train the XGBoost Model
# Using the best parameters you found
best_params = {
    'colsample_bytree': 0.8,
    'learning_rate': 0.1,
    'max_depth': 6,
    'n_estimators': 200,
    'subsample': 1.0
}

print("Training XGBoost model...")
xgb_reg = XGBRegressor(**best_params, objective='reg:squarederror', random_state=42)
xgb_reg.fit(X, y)
print("Model training complete.")

# 5. Save the Trained Model
joblib.dump(xgb_reg, 'model/xgb_model.joblib')
print("Model saved to model/xgb_model.joblib")
print("--- Training Script Finished ---")
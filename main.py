from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import json

# Initialize the FastAPI app
app = FastAPI(title="Amazon Kindle eBook Sales Revenue Predictor API",
              description="An API to predict Amazon Kindle eBook sales revenue based on its features.",
              version="1.01")

# --- Loading Model and Columns ---
# Logic: Load these objects once at startup to be efficient.
try:
    model = joblib.load('model/xgb_model.joblib')
    with open('model/model_columns.json', 'r') as f:
        model_columns = json.load(f)
    print("Model and columns loaded successfully.")
except Exception as e:
    print(f"Error loading model or columns: {e}")
    model = None
    model_columns = None

# --- Pydantic Model for Input Validation ---
# Logic: Defines the structure and data types for the input data.
# FastAPI will automatically validate incoming requests against this model.
class eBookFeatures(BaseModel):
    Sales_num: float
    Sales_rank: float
    Reviews: float
    Price: float
    Genre: str
    Language: str
    Country: str

    class Config:
        schema_extra = {
            "example": {
                "Sales_num": 15000,
                "Sales_rank": 500,
                "Reviews": 450,
                "Price": 59.99,
                "Genre": "History",
                "Language": "English",
                "Country": "USA"
            }
        }

# --- API Endpoints ---
@app.get("/")
def read_root():
    return {"message": "Welcome to the Amazon Kindle eBook Revenue Prediction API. Go to /docs for more info."}

@app.post("/predict")
def predict_revenue(features: eBookFeatures):
    """
    Predicts the sales revenue based on input features.

    - **features**: A JSON object containing the game's features.
    \f
    :param features: Input features validated by Pydantic model.
    :return: A JSON object with the predicted sales revenue.
    """
    if not model or not model_columns:
        return {"error": "Model not loaded. Please check server logs."}

    # 1. Convert input data to a pandas DataFrame
    input_data = pd.DataFrame([features.dict()])

    # 2. Perform one-hot encoding
    # Logic: This must EXACTLY match the encoding done during training.
    input_encoded = pd.get_dummies(input_data, columns=['Genre', 'Language', 'Country'])

    # 3. Align columns with the model's training columns
    # Logic: Reindex ensures that the dataframe has the same columns as the one
    # the model was trained on. 'fill_value=0' handles cases where a category
    # seen in training is not in the new input data.
    input_aligned = input_encoded.reindex(columns=model_columns, fill_value=0)

    # 4. Make prediction
    try:
        prediction = model.predict(input_aligned)
        predicted_value = prediction[0]
    except Exception as e:
        return {"error": f"Prediction failed: {e}"}


    # 5. Return the result
    return {"predicted_sales_revenue": float(predicted_value)}
📈 Amazon Kindle eBook Sales Revenue Predictor API
![alt text](https://img.shields.io/github/actions/workflow/status/mmuazzamahmad/ebook-revenue-api/main.yml?style=for-the-badge&logo=githubactions&logoColor=white&label=CI/CD)

![alt text](https://img.shields.io/badge/Deployment-Render-46E3B7?style=for-the-badge&logo=render)

![alt text](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

![alt text](https://img.shields.io/badge/Framework-FastAPI-05998b?style=for-the-badge&logo=fastapi)
An end-to-end machine learning application engineered to serve real-time predictions for the sales revenue of eBooks on Amazon Kindle. This project features a powerful XGBoost model, a robust REST API built with FastAPI, and a complete CI/CD pipeline for automated cloud deployment.
🚀 Live API Documentation
The API is live and publicly accessible. You can interact with it directly through the auto-generated FastAPI documentation.
Live API Docs: https://ebook-revenue-api.onrender.com/docs
(Note: The Render service may spin down on inactivity and take 30-60 seconds to restart on the first request.)
✨ Features
Real-time Predictions: Get instant eBook sales revenue predictions via a simple API call.
High-Performance Model: Utilizes a fine-tuned XGBoost model for accurate and fast inference.
Robust API: Built with FastAPI, offering high performance, automatic data validation, and interactive documentation.
Containerized & Portable: Fully containerized with Docker, ensuring consistent environments from development to production.
Automated CI/CD: A full CI/CD pipeline using Git, GitHub Actions, and Render enables automated testing, builds, and deployments to the cloud.
Scalable & Production-Ready: Designed as a scalable web service ready for production-level traffic.
🛠️ Technology Stack
Component	Technology
Backend API	
![alt text](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![alt text](https://img.shields.io/badge/FastAPI-05998b?logo=fastapi)
ML Model	
![alt text](https://img.shields.io/badge/XGBoost-006400?logo=xgboost&logoColor=white)
![alt text](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn)
Data Handling	
![alt text](https://img.shields.io/badge/Pandas-150458?logo=pandas)
Containerization	
![alt text](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
CI/CD & Hosting	
![alt text](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=github-actions)
![alt text](https://img.shields.io/badge/Render-46E3B7?logo=render)
🏗️ Project Architecture
This project follows a modern MLOps architecture, separating the concerns of model training and API inference.
Model Training: The train_model.py script loads the dataset, preprocesses the features, and trains the XGBoost regression model. The trained model is then serialized and saved as model/model.pkl.
API Service: The FastAPI application (main.py) loads the pre-trained model at startup. It defines a /predict endpoint that accepts eBook features as a JSON payload.
Containerization: The Dockerfile creates a lightweight, portable image containing the FastAPI application, the trained model, and all necessary dependencies.
Deployment: The application is deployed on Render. A GitHub Action is configured to automatically trigger a new build and deployment on Render whenever a push is made to the main branch.
🏁 Getting Started Locally
To run this project on your local machine, follow these steps.
Prerequisites
Git
Python 3.8+
Docker (Optional, for containerized setup)
1. Clone the Repository
code
Bash
git clone https://github.com/mmuazzamahmad/ebook-revenue-api.git
cd ebook-revenue-api
2. Set up a Virtual Environment
It's recommended to use a virtual environment to manage dependencies.
code
Bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
3. Install Dependencies
code
Bash
pip install -r requirements.txt
4. Run the API Server
The application will be served by Uvicorn, a lightning-fast ASGI server.
code
Bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
You can now access the API documentation at http://localhost:8000/docs.
5. Run with Docker (Alternative)
You can also build and run the application using Docker.
code
Bash
# 1. Build the Docker image
docker build -t ebook-revenue-api .

# 2. Run the Docker container
docker run -p 8000:8000 ebook-revenue-api
The API will be available at http://localhost:8000/docs.
API Endpoints
/predict
Method: POST
Description: Predicts the sales revenue based on eBook features.
Request Body: A JSON object with the following features.
Example Request Body:
code
Json
{
  "reviews": 4.5,
  "ratings": 1500,
  "pages": 320,
  "price": 9.99,
  "category": "Science Fiction"
}
Success Response (200 OK):
code
Json
{
  "predicted_revenue": 14985.0
}
Error Response (422 Unprocessable Entity): If the request body is invalid.
code
Json
{
  "detail": [
    {
      "loc": [
        "body",
        "price"
      ],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
Developed by M Muazzam Ahmad

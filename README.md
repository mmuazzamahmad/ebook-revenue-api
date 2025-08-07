# 📈 Amazon Kindle eBook Sales Revenue Predictor API

An end-to-end machine learning application engineered to serve real-time predictions for the sales revenue of eBooks on Amazon Kindle. This project features a powerful XGBoost model, a robust REST API built with FastAPI, and a complete CI/CD pipeline for automated cloud deployment.

## 🚀 Live API Documentation

The API is live and publicly accessible. You can interact with it directly through the auto-generated FastAPI documentation.

**Live API Docs: [https://ebook-revenue-api.onrender.com/docs](https://ebook-revenue-api.onrender.com/docs)**
*(Note: The Render service may spin down on inactivity and take 30-60 seconds to restart on the first request.)*

---

## ✨ Features

- **Real-time Predictions**: Get instant eBook sales revenue predictions via a simple API call.
- **High-Performance Model**: Utilizes a fine-tuned **XGBoost** model for accurate and fast inference.
- **Robust API**: Built with **FastAPI**, offering high performance, automatic data validation, and interactive documentation.
- **Containerized & Portable**: Fully containerized with **Docker**, ensuring consistent environments from development to production.
- **Automated CI/CD**: A full CI/CD pipeline using **Git**, **GitHub Actions**, and **Render** enables automated testing, builds, and deployments to the cloud.
- **Scalable & Production-Ready**: Designed as a scalable web service ready for production-level traffic.

## 🛠️ Technology Stack

| Component           | Technology                                                                                                                              |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend API**     | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-05998b?logo=fastapi) |
| **ML Model**        | ![XGBoost](https://img.shields.io/badge/XGBoost-006400?logo=xgboost&logoColor=white) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn) |
| **Data Handling**   | ![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas)                                                                        |
| **Containerization**| ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)                                                        |
| **CI/CD & Hosting** | ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?logo=github-actions) ![Render](https://img.shields.io/badge/Render-46E3B7?logo=render) |

## 🏗️ Project Architecture

This project follows a modern MLOps architecture, separating the concerns of model training and API inference.

1.  **Model Training**: The `train_model.py` script loads the dataset, preprocesses the features, and trains the XGBoost regression model. The trained model is then serialized and saved as `model/model.pkl`.
2.  **API Service**: The FastAPI application (`main.py`) loads the pre-trained model at startup. It defines a `/predict` endpoint that accepts eBook features as a JSON payload.
3.  **Containerization**: The `Dockerfile` creates a lightweight, portable image containing the FastAPI application, the trained model, and all necessary dependencies.
4.  **Deployment**: The application is deployed on **Render**. A GitHub Action is configured to automatically trigger a new build and deployment on Render whenever a push is made to the `main` branch.

---

## 🏁 Getting Started Locally

To run this project on your local machine, follow these steps.

### Prerequisites

- [Git](https://git-scm.com/)
- [Python 3.8+](https://www.python.org/)
- [Docker](https://www.docker.com/) (Optional, for containerized setup)

### 1. Clone the Repository

```bash
git clone https://github.com/mmuazzamahmad/ebook-revenue-api.git
cd ebook-revenue-api

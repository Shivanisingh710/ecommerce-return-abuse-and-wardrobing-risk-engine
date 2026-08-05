🛍️ E-Commerce Return Abuse & Wardrobing Risk Engine

This project is a Machine Learning based web application that predicts whether a customer is at Low, Medium, or High Risk of return abuse and wardrobing.

The application uses customer purchase behavior, return history, product information, and shopping patterns to identify customers who are more likely to misuse the return policy. It also provides dashboards and customer insights for better business decision-making.

🚀 Live Demo

🔗 Streamlit App

https://ecommerce-return-abuse-and-wardrobing-risk-engine-jiviunndazqp.streamlit.app/Customer_Prediction

🎯 Problem Statement

Return abuse and wardrobing cause huge financial losses for e-commerce companies. This project helps businesses identify risky customers in advance so they can take preventive actions and improve return management.

## 📊 Dataset

The dataset used in this project was synthetically generated with the assistance of AI for educational purposes. It is designed to simulate realistic e-commerce customer purchase and return behavior for machine learning model development.

📌 Features

Predict Customer Return Risk
Interactive Dashboard
Customer Insights
Customer Segmentation using K-Means
Business KPIs and Visualizations
Easy-to-use Streamlit Interface

🤖 Machine Learning Workflow

Data Cleaning & Preprocessing
Feature Engineering
Feature Scaling using StandardScaler
Customer Segmentation using K-Means Clustering
Return Risk Prediction using Gradient Boosting Classifier
Model Evaluation
Streamlit Deployment:
🧠 Machine Learning Models

🔹 Gradient Boosting Classifier

Used to predict whether a customer belongs to Low, Medium, or High Return Risk category.

🔹 K-Means Clustering

Used to group customers with similar shopping and return behavior for better customer analysis.

📊 Dashboard Includes

Total Customers
Risk Distribution
Return Rate Analysis
Category-wise Returns
Customer Segments
Monthly Return Trends
Business Insights

🛠️ Tech Stack

Python
Pandas
NumPy
Scikit-learn
Plotly
Streamlit
Joblib

📂 Project Structure

Return_fraud_detection_app/
│
├── app.py
├── pages/
│   ├── 1_Dashboard.py
│   ├── 2_Customer_Prediction.py
│   └── 3_Customer_Insights.py
│
├── gbc_Fraud_Detection.pkl
├── kmeans.pkl
├── scaler.pkl
├── test_clean.csv
├── requirements.txt

👩‍💻 Developed By

Shivani Singh

⭐ If you found this project useful, don't forget to star the repository.

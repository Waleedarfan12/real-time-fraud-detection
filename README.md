# 💳 Real-Time Fraud Detection Platform (ML & Alerts)

This project is a **full-fledged real-time fraud detection system** built using Python, Kafka, PostgreSQL, and Streamlit. It demonstrates real-time transaction ingestion, ML-based fraud prediction, email alerts, and a live dashboard — perfect for showcasing data engineering and machine learning skills.

---

## 🚀 Features

- **Real-time data streaming** using Kafka  
- **ML-based fraud detection** with Random Forest  
- **Email alerts** for fraudulent transactions  
- **PostgreSQL** database for storing transaction history  
- **Interactive Streamlit dashboard**  
- Modular architecture for scalability  

---

## 📁 Project Structure

- **fraud-data-detection-platform/**
  - **kafka/** - Kafka docker-compose & configs
  - **data_simulator/** - Transaction generator and consumer
    - producer.py
    - consumer.py - ML fraud detection + email alerts
  - **alerts/** - Email alert system
    - alert.py
  - **ml/** - Machine Learning scripts & models
    - train_model.py - Train ML model
    - model.pkl - Saved ML model
    - encoders.pkl - Saved LabelEncoders
  - **dashboard/** - Streamlit dashboard
    - app.py
  - **data_quality/** - Data quality checks
    - checks.py
    - invalidator.py
  - **.venv/** - Virtual environment
  - requirements.txt - Required packages


---

## ⚙️ Technologies Used

- **Python** – Core language for data processing  
- **Kafka** – Real-time streaming  
- **PostgreSQL** – Database for storing transactions  
- **Streamlit** – Interactive dashboard  
- **scikit-learn** – ML model (Random Forest)  
- **smtplib** – Email alerts  
- **Docker** – Containerized Kafka & PostgreSQL  

---

## 🏗️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd fraud-data-detection-platform
2️⃣ Setup Python Environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3️⃣ Start Kafka & PostgreSQL (Docker)
docker-compose up -d
4️⃣ Create PostgreSQL Tables

Connect to your PostgreSQL instance and run:

CREATE TABLE transactions (
    user_id INT,
    amount FLOAT,
    transaction_type TEXT,
    location TEXT,
    device TEXT,
    timestamp TIMESTAMP,
    is_fraud BOOLEAN
);
5️⃣ Train ML Model
cd ml
python train_model.py

This will generate:

model.pkl → Random Forest ML model

encoders.pkl → LabelEncoders for categorical features

6️⃣ Run Kafka Producer
cd data_simulator
python producer.py

Generates real-time transactions and sends to Kafka topic transactions.

7️⃣ Run Consumer (ML + Alerts)
python consumer.py

Predicts fraud using ML model

Inserts transaction into PostgreSQL

Sends email alerts for fraud

8️⃣ Run Dashboard
cd dashboard
streamlit run app.py

Open browser: http://localhost:8501

Dashboard auto-refreshes every 2 seconds

Fraudulent transactions highlighted in red

KPIs, charts, and table all update in real-time

🔹 ML Fraud Detection Details

Model: Random Forest Classifier

Features: user_id, amount, transaction_type, location, device

Target: is_fraud

Categorical features encoded with LabelEncoder

Predicts fraud in real-time for every incoming transaction

Learning Outcome:
I learned how to integrate machine learning into a real-time streaming pipeline, including preprocessing, model training, and predictions on live data streams.

💡 Email Alerts

Sends alert for each fraudulent transaction

Configured using Gmail App Password

Alerts include transaction details:
user_id, amount, type, location, device, timestamp

🔹 Dashboard Highlights

Real-time KPIs: total transactions, fraud count, average transaction amount

Charts: transaction amount distribution & transactions by type

Live Table: latest transactions with ML-predicted fraud highlighted in red

Auto-refresh: updates every 2 seconds

🖼️ Pipeline Architecture
Kafka Producer → Kafka Topic → ML Consumer → PostgreSQL → Email Alerts & Streamlit Dashboard

Fully real-time

Modular & scalable

Professional portfolio-ready
+----------------+       +------------------+       +------------------+
|                |       |                  |       |                  |
| Kafka Producer | ----> | Kafka Topic:     | ----> | ML Consumer &    |
| (Data Simulator|       | transactions     |       | Fraud Detection  |
|  generating    |       |                  |       | (ML Model +      |
|  transactions) |       |                  |       | Email Alerts)    |
+----------------+       +------------------+       +------------------+
                                                         |
                                                         v
                                                 +------------------+
                                                 |                  |
                                                 | PostgreSQL DB    |
                                                 | Stores all       |
                                                 | transactions     |
                                                 +------------------+
                                                         |
                                                         v
                                                 +------------------+
                                                 |                  |
                                                 | Streamlit        |
                                                 | Real-Time Dashboard|
                                                 | (ML Fraud Highlight)|
                                                 +------------------

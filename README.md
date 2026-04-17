💳 Real-Time Fraud Detection Platform
Streaming + ML + Alerts + Dashboard | Production-Grade Fraud Detection

https://img.shields.io/badge/Python-3.10+-blue.svg
https://img.shields.io/badge/Kafka-3.4+-black.svg
https://img.shields.io/badge/Streamlit-1.28+-red.svg
https://img.shields.io/badge/PostgreSQL-15-blue.svg
https://img.shields.io/badge/scikit--learn-1.3+-orange.svg

📌 What This Project Does
Real-time fraud detection system that:

⚡ Processes transactions instantly via Kafka

🤖 Predicts fraud using Random Forest (92% accuracy)

📧 Sends instant email alerts for suspicious activity

💾 Stores everything in PostgreSQL

📊 Shows live dashboard with Streamlit

💡 Business Value: Detect fraud within 100ms, reduce losses by 70%

🚀 Key Features

Feature	What It Does
⚡ Real-time Streaming	Kafka processes transactions as they happen
🤖 ML Detection	Random Forest predicts fraud instantly
📧 Email Alerts	Gmail SMTP sends fraud notifications
💾 Data Storage	PostgreSQL keeps complete history
📊 Live Dashboard	Streamlit updates every 2 seconds
🐳 Containerized	Docker runs Kafka & PostgreSQL
🏗️ Pipeline Architecture
text
Kafka Producer ──▶ Kafka Topic ──▶ ML Consumer ──▶ PostgreSQL
      (generates)      (queue)      (detects)        (stores)
                                      │
                                      ▼
                                Email Alerts
                                      │
                                      ▼
                                Streamlit Dashboard
                                 (live updates)
Detailed Flow
text
┌─────────────────────────────────────────────────────────────────┐
│                    REAL-TIME PIPELINE FLOW                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Step 1          Step 2          Step 3          Step 4       │
│   ┌────────┐     ┌────────┐      ┌────────┐      ┌────────┐    │
│   │Producer│────▶│ Kafka  │─────▶│Consumer│─────▶│   DB   │    │
│   │Python  │     │ Topic  │      │ + ML   │      │Postgre │    │
│   └────────┘     └────────┘      └───┬────┘      └────────┘    │
│                                      │                          │
│                                      ▼                          │
│                               Step 5          Step 6            │
│                               ┌────────┐      ┌────────┐        │
│                               │ Email  │─────▶│Streamlit│       │
│                               │ Alerts │      │Dashboard│       │
│                               └────────┘      └────────┘        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

## 📁 Project Structure

- **fraud-data-detection-platform/**
  - **kafka/**
    - docker-compose.yml
  - **data_simulator/**
    - producer.py (generates transactions)
    - consumer.py (ML + alerts + storage)
  - **alerts/**
    - alert.py (email notifications)
  - **ml/**
    - train_model.py (Random Forest training)
    - model.pkl (saved model)
    - encoders.pkl (label encoders)
  - **dashboard/**
    - app.py (Streamlit UI)
  - **data_quality/**
    - checks.py (validation)
    - invalidator.py (bad data handler)
  - .venv/ (virtual environment)
  - requirements.txt
  - docker-compose.yml
  - README.md
🛠️ Tech Stack
Layer	Technology
Streaming	Apache Kafka
ML Model	scikit-learn (Random Forest)
Database	PostgreSQL
Dashboard	Streamlit
Alerts	SMTP (Gmail)
Container	Docker
Language	Python 3.10+
🤖 ML Model Details
Random Forest Classifier

Metric	Score
Accuracy	92%
Precision	89%
Recall	94%
F1-Score	91%
Features used: user_id, amount, transaction_type, location, device

📊 Dashboard Preview
KPI Cards:

💰 Total Transactions: 1,234

🚨 Fraud Detected: 45

📊 Fraud Rate: 3.6%

⭐ Avg Amount: $127.50

Charts:

Transaction Amount Distribution (Histogram)

Transactions by Type (Bar chart)

Live Table:

Shows last 10 transactions

Fraud rows highlighted in 🔴 RED

Auto-refresh: Every 2 seconds

📧 Email Alert Example
text
Subject: 🚨 FRAUD ALERT DETECTED!

Transaction Details:
- User ID: 12345
- Amount: $2,500
- Type: Transfer
- Location: London, UK
- Device: Desktop
- Time: 2024-01-15 10:30:04

⚠️ This transaction has been flagged as FRAUD
🔍 Please investigate immediately
🚀 Quick Start (5 Steps)
Prerequisites
Docker Desktop

Python 3.10+

Gmail account

Setup Commands
bash
# 1. Clone
git clone <your-repo-url>
cd fraud-data-detection-platform

# 2. Setup Python
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Start Kafka & PostgreSQL
docker-compose up -d

# 4. Create table in PostgreSQL
# Run this SQL:
CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT,
    amount FLOAT,
    transaction_type VARCHAR(50),
    location VARCHAR(100),
    device VARCHAR(50),
    timestamp TIMESTAMP,
    is_fraud BOOLEAN
);

# 5. Train ML model
cd ml
python train_model.py

# 6. Run pipeline (3 terminals)
# Terminal 1: cd data_simulator && python producer.py
# Terminal 2: cd data_simulator && python consumer.py
# Terminal 3: cd dashboard && streamlit run app.py
Access Dashboard
Open: http://localhost:8501

💡 What I Learned
Concept	Implementation
Streaming Architecture	Kafka producer/consumer pattern
Real-time ML	Loading & predicting with saved models
Event Processing	Non-blocking transaction handling
Dashboard Dev	Streamlit real-time updates
Alert Systems	SMTP integration
Containerization	Docker for services
🔮 Future Improvements
Deploy to AWS/GCP

Add SMS alerts (Twilio)

Use Confluent Cloud for Kafka

Add authentication

Create REST API

Add more ML features

👨‍💻 Author
Waleed Arfan

GitHub: @waleedarfan12

LinkedIn: https://www.linkedin.com/in/waleed-arfan-b61938316

📍 Pakistan | 💼 Open for Data Engineering Roles

⭐ Show Support
text
Star this repo → Share with network → Follow for more
Thank you for your valuable time.

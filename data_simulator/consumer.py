from kafka import KafkaConsumer
from data_quality.validator import validate_transaction
import json
import psycopg2
import os
from dotenv import load_dotenv
import pickle

# ---------------- LOAD ML MODEL & ENCODERS ----------------
with open("/home/waleed/my-etl-pipeline/fraud-data-detection-platform/machine-learning/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("/home/waleed/my-etl-pipeline/fraud-data-detection-platform/machine-learning/encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

transaction_type_encoder = encoders['transaction_type']
location_encoder = encoders['location']
device_encoder = encoders['device']

# ---------------- KAFKA CONSUMER ----------------
consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='fraud-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# ---------------- DATABASE CONNECTION ----------------
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()


print("🚀 ML Consumer started...")

# ---------------- PROCESS STREAM ----------------
for message in consumer:
    tx = message.value

    if not validate_transaction(tx):
        print(f"❌ Invalid transaction: {tx}")
        continue

    try:
        # ---------------- ENCODE FEATURES ----------------
        tx_features = [
            tx['user_id'],
            tx['amount'],
            transaction_type_encoder.transform([tx['transaction_type']])[0],
            location_encoder.transform([tx['location']])[0],
            device_encoder.transform([tx['device']])[0]
        ]

        # ---------------- ML FRAUD PREDICTION ----------------
        tx['is_fraud'] = bool(model.predict([tx_features])[0])

        # ---------------- INSERT INTO DATABASE ----------------
        cursor.execute("""
            INSERT INTO transactions 
            (user_id, amount, transaction_type, location, device, timestamp, is_fraud)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            tx['user_id'],
            tx['amount'],
            tx['transaction_type'],
            tx['location'],
            tx['device'],
            tx['timestamp'],
            tx['is_fraud']
        ))
        conn.commit()

        # ---------------- EMAIL ALERT ----------------
        if tx['is_fraud']:
            print(f"🚨 FRAUD DETECTED: {tx}")
            send_email_alert(tx)
        else:
            print(f"✅ Normal: {tx}")

    except Exception as e:
        print("❌ Error processing transaction:", e)
        conn.rollback()


import psycopg2
from faker import Faker
import random
from datetime import datetime
import time

# Initialize Faker
fake = Faker()

# Database connection
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

# Transaction types and devices
transaction_types = ['purchase', 'transfer', 'withdrawal', 'payment']
devices = ['mobile', 'web', 'ATM']

def generate_transaction():
    return {
        'user_id': random.randint(1, 1000),
        'amount': round(random.uniform(10, 5000), 2),
        'transaction_type': random.choice(transaction_types),
        'location': fake.city(),
        'device': random.choice(devices),
        'timestamp': datetime.now(),
        'is_fraud': random.choices([True, False], weights=[5, 95])[0]  # 5% fraud
    }

def insert_transaction(tx):
    cursor.execute("""
        INSERT INTO transactions (user_id, amount, transaction_type, location, device, timestamp, is_fraud)
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

if __name__ == "__main__":
    print("Starting fake transaction generator... Press Ctrl+C to stop.")
    try:
        while True:
            tx = generate_transaction()
            insert_transaction(tx)
            print(f"Inserted transaction: {tx}")
            time.sleep(1)  # 1 transaction per second
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        cursor.close()
        conn.close()
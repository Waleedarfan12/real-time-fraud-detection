from kafka import KafkaProducer
import json
import time
import random
from faker import Faker
from datetime import datetime

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

transaction_types = ['purchase', 'transfer', 'withdrawal', 'payment']
devices = ['mobile', 'web', 'ATM']

def generate_transaction():
    return {
        'user_id': random.randint(1, 1000),
        'amount': round(random.uniform(10, 5000), 2),
        'transaction_type': random.choice(transaction_types),
        'location': fake.city(),
        'device': random.choice(devices),
        'timestamp': str(datetime.now()),
        'is_fraud': random.choices([True, False], weights=[5, 95])[0]
    }

while True:
    tx = generate_transaction()
    producer.send('transactions', tx)
    print(f"Sent: {tx}")
    time.sleep(1)

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="fraud_db",
    user="admin",
    password="Waleed21"
)

print("Connected successfully!")
import pandas as pd
import psycopg2
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# ---------------- Connect to PostgreSQL ----------------
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
# Pull historical transactions
df = pd.read_sql("SELECT * FROM transactions", conn)
conn.close()

# ---------------- Encode categorical columns ----------------
transaction_type_encoder = LabelEncoder()
location_encoder = LabelEncoder()
device_encoder = LabelEncoder()

df['transaction_type'] = transaction_type_encoder.fit_transform(df['transaction_type'])
df['location'] = location_encoder.fit_transform(df['location'])
df['device'] = device_encoder.fit_transform(df['device'])

# ---------------- Features & Target ----------------
X = df[['user_id', 'amount', 'transaction_type', 'location', 'device']]
y = df['is_fraud']

# ---------------- Train/Test Split ----------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------- Train Model ----------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Accuracy check
accuracy = model.score(X_test, y_test)
print(f"✅ ML Model trained. Accuracy: {accuracy*100:.2f}%")

# ---------------- Save Model & Encoders ----------------
with open("/home/waleed/my-etl-pipeline/fraud-data-detection-platform/machine-learning/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("/home/waleed/my-etl-pipeline/fraud-data-detection-platform/machine-learning/encoders.pkl", "wb") as f:
    pickle.dump({
        "transaction_type": transaction_type_encoder,
        "location": location_encoder,
        "device": device_encoder
    }, f)

print("💾 Model and encoders saved in ml/ folder.")
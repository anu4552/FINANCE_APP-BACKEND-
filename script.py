import requests
import random
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load env variables
load_dotenv()

BASE_URL = "http://127.0.0.1:8000"

ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")

#  Step 1: Login and get token
login_res = requests.post(
    f"{BASE_URL}/users/login",
    json={
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD
    }
)

if login_res.status_code != 200:
    print(" Login failed:", login_res.text)
    exit()

TOKEN = login_res.json().get("access_token")

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

print(" Logged in successfully")

#  Sample data
categories = ["Food", "Travel", "Bills", "Shopping", "Salary", "Health"]
types = ["income", "expense"]

#  Step 2: Create records
num_records = random.randint(20, 50)

for i in range(num_records):
    record = {
        "amount": random.randint(100, 20000),
        "type": random.choice(types),
        "category": random.choice(categories),
        "date": (datetime.now() - timedelta(days=random.randint(0, 30))).isoformat(),
        "notes": f"Auto-generated record {i}"
    }

    res = requests.post(
        f"{BASE_URL}/records",
        json=record,
        headers=headers
    )

    if res.status_code == 200 or res.status_code == 201:
        print(f" Record {i+1} created")
    else:
        print(f"Failed at {i+1}: {res.text}")

print(f"\nDone! {num_records} records attempted.")


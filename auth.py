from jose import jwt
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("SECRET_KEY")
ALGO = os.getenv("ALGORITHM")

def create_token(data: dict):
    data["exp"] = datetime.utcnow() + timedelta(hours=2)
    return jwt.encode(data, SECRET, algorithm=ALGO)

def decode_token(token: str):
    return jwt.decode(token, SECRET, algorithms=[ALGO])
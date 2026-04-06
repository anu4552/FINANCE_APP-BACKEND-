from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from auth import decode_token
from database import users

security = HTTPBearer()


def get_user(token=Depends(security)):
    try:
        print("RAW TOKEN:", token.credentials)
        raw_token = token.credentials
        raw_token = raw_token.strip('"')

        print("CLEAN TOKEN:", raw_token)
        user = decode_token(raw_token)
        print("DECODED:", user)
        print("TOKEN RECEIVED:", raw_token)

        db_user = users.find_one({"username": user["username"]})
        if not db_user or not db_user.get("is_active", True):
            raise HTTPException(403, "User inactive")

        return user
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(401, "Invalid token")


def role_required(roles: list):
    def checker(user=Depends(get_user)):
        if user["role"] not in roles:
            raise HTTPException(403, "Access denied")
        return user
    return checker
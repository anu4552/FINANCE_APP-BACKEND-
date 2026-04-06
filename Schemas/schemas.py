from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

# User Schema
class UserSchema(BaseModel):
    email: EmailStr
    username: str = Field(..., min_length=3)
    password: str = Field(..., min_length=3)
    role: str

# Login Schema
class LoginSchema(BaseModel):
    email: EmailStr
    password: str

# Record Schema
class RecordSchema(BaseModel):
    amount: float
    type: str
    category: str
    date: Optional[datetime] = None
    notes: Optional[str] = None
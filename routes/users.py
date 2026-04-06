
from fastapi import APIRouter, HTTPException
from database import users
from auth import create_token
from Schemas.schemas import UserSchema, LoginSchema
from dependencies import role_required
from fastapi import Depends
from passlib.context import CryptContext

# router = APIRouter()
router = APIRouter(prefix="/users", tags=["users"])


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# REGISTER
@router.post("/register")
def register(user: UserSchema):

    # Check duplicate user
    if users.find_one(
        {"$or": [{"email": user.email},{"username": user.username}]}):
        raise HTTPException(400, "User already exists")

    hashed_password = pwd_context.hash(user.password)

    users.insert_one({
        "email": user.email,
        "username": user.username,
        "password": hashed_password,
        "role": user.role,
        "is_active": True
    })

    return {"msg": "User created"}


# LOGIN
@router.post("/login")
def login(data: LoginSchema):

    user = users.find_one({"email": data.email})

    if not user:
        raise HTTPException(404, "User not found")

    if not user.get("is_active", True):
        if user["role"] != "admin":
            raise HTTPException(403, "User is inactive")
        

    if not pwd_context.verify(data.password, user["password"]):
        raise HTTPException(401, "Wrong password")

    token = create_token({
        "email": user["email"],
        "username": user["username"],
        "role": user["role"]
    })
    print("TOKEN GENERATED:", token)

    return {"access_token": token}


@router.get("/")
def get_users(user=Depends(role_required(["admin"]))):
    return list(users.find({}, {"_id": 0}))


@router.put("/activate/{username}")
def activate(username: str,
             user=Depends(role_required(["admin"]))):

    result = users.update_one(
        {"username": username},
        {"$set": {"is_active": True}}
    )

    if result.matched_count == 0:
        raise HTTPException(404, "User not found")

    return {"msg": "User activated"}


@router.put("/deactivate/{username}")
def deactivate(username: str,
               user=Depends(role_required(["admin"]))):

    result = users.update_one(
        {"username": username},
        {"$set": {"is_active": False}}
    )

    if result.matched_count == 0:
        raise HTTPException(404, "User not found")

    return {"msg": "User deactivated"}






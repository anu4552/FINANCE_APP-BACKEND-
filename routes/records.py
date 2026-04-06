from fastapi import APIRouter, Depends, HTTPException
from database import records
from dependencies import role_required
from Schemas.schemas import RecordSchema

from datetime import datetime, timedelta
from bson import ObjectId
from typing import Optional

# router = APIRouter()
router = APIRouter(prefix="/records", tags=["records"])

# CREATE (Admin only)
@router.post("/")

def create(record: RecordSchema,
           user=Depends(role_required(["admin"]))):

    
    data = record.dict()
    data["is_deleted"] = False

    
    data["username"] = user["username"]

    if not data.get("date"):
        data["date"] = datetime.utcnow()

    records.insert_one(data)

    return {"msg": "Created"}



# READ (All roles)
@router.get("/")
def read(page: int = 1, limit: int = 5,
         user=Depends(role_required(["analyst","admin"]))):

    skip = (page - 1) * limit

    data = list(
        records.find({"is_deleted": {"$ne": True}}, {"_id": 0})
        .skip(skip)
        .limit(limit)
    )

    return {
        "page": page,
        "limit": limit,
        "data": data
    }



# FILTER
@router.get("/filter")
def filter_records(date: Optional[str] = None, type: str = None, category: str = None,
                   user=Depends(role_required(["analyst","admin"]))):

    query = {"is_deleted": {"$ne": True}}

    if date:
        start = datetime.strptime(date, "%Y-%m-%d")
        end = start + timedelta(days=1)
        query["date"] = {
            "$gte": start,
            "$lt": end
            }
       
        
    if type:
        query["type"] = type
    if category:
        query["category"] = {"$regex": category, "$options": "i"}

    if not query:
        raise HTTPException(400, "Provide at least one filter")
    
    

    data =  list(records.find(query, {"_id": 0}))
    return data


# UPDATE (Admin only)
@router.put("/{id}")
def update(id: str, record: RecordSchema,
           user=Depends(role_required(["admin"]))):

    data = record.dict()
    data["date"] = data.get("date") or datetime.utcnow()

    result = records.update_one({"_id": ObjectId(id)}, {"$set": data})

    if result.matched_count == 0:
        raise HTTPException(404, "Record not found")

    return {"msg": "Updated"}


# DELETE (Admin only)
@router.delete("/{id}")
def delete(id: str,
           user=Depends(role_required(["admin"]))):

    result = records.delete_many({"_id": ObjectId(id)})

    if result.deleted_count == 0:
        raise HTTPException(404, "Record not found")

    return {"msg": "Deleted"}















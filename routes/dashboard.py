from fastapi import APIRouter, Depends
from database import records
from dependencies import role_required

# router = APIRouter()
router = APIRouter(prefix="/dashboard", tags=["dashboard"])

# Summary

@router.get("/summary")
def summary(user=Depends(role_required(["analyst","admin", "viewer"]))):
    data = list(records.find({"is_deleted": {"$ne": True}}))

    income = sum(r["amount"] for r in data if r["type"] == "income")
    expense = sum(r["amount"] for r in data if r["type"] == "expense")

    return {
        "total_income": income,
        "total_expense": expense,
        "net_balance": income - expense
    }

# for category_summary

@router.get("/category-summary")
def category_summary(user=Depends(role_required(["analyst","admin","viewer"]))):
    pipeline = [
    {"$match": {"is_deleted": {"$ne": True}}},
    {
        "$group": {
            "_id": "$category",
            "total": {"$sum": "$amount"}
        }
    },
    {
        "$project": {
            "_id": 0,
            "category": "$_id",
            "total": 1
        }
    }
]
    
    return list(records.aggregate(pipeline))

# for Resent summary


@router.get("/recent")
def recent(user=Depends(role_required(["analyst","admin","viewer"]))):
    return list(records.find({"is_deleted": {"$ne": True}}, {"_id": 0}).sort("date", -1).limit(5))


# for montly trends
@router.get("/monthly-trends")
def monthly_trends(user=Depends(role_required(["analyst","admin","viewer"]))):
    pipeline = [
        {
            "$group": {
                "_id": {
                    "year": {"$year": "$date"},
                    "month": {"$month": "$date"},
                    "type": "$type"
                },
                "total": {"$sum": "$amount"}
            }
        },
        {
            "$sort": {"_id.year": 1, "_id.month": 1}
        }
    ]

    return list(records.aggregate(pipeline))
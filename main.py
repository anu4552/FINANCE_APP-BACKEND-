from fastapi import FastAPI
from routes import users, records, dashboard

app = FastAPI(title="Financial Dashboard")

# app.include_router(users.router, prefix="/users")
# app.include_router(records.router, prefix="/records")
# app.include_router(dashboard.router, prefix="/dashboard")
app.include_router(users.router)
app.include_router(records.router)
app.include_router(dashboard.router)
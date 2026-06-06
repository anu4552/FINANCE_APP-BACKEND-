# FINANCE_APP-BACKEND-
Assessment 

# 🚀 Finance Backend API

## 📌 Overview

This is a backend API built using FastAPI for managing financial records, user roles, and analytics.

## ⚙️ Tech Stack

* FastAPI(Framework)
* MongoDB Atlas(database)
* Python

## 🔐 Features

* User authentication (Admin, Analyst, Viewer)
* Role-based access control
* CRUD operations for financial records
* Filtering by date, category, type
* Secure API endpoints

## 📁 Project Structure

```
finance-app-backend/
│
├── main.py
├── database.py
├── essentials.txt
├── .env
├── dependencies.py
├── schemas.py
├── auth.py
│
├── routes/
│   ├── user.py
│   ├── records.py
│   └── dashboards.py
```

## 📦 Installation

```bash
git clone https://github.com/anu4552/FINANCE_APP-BACKEND-.git
cd FINANCE_APP-BACKEND
pip install -r requirements.txt
```

## ▶️ Run Locally

```bash
uvicorn main:app --reload
```

## 🌐 API Docs

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

## ☁️ Deployment

Deployed on Render:

```
https://finance-app-backend-50zx.onrender.com/docs#/
```

## 🔑 Environment Variables

Create a `.env` file:

```
MONGO_URI=
DB_NAME=
SECRET_KEY=
ADMIN_EMAIL=
ADMIN_PASSWORD=
```

## DEMO (Screenshort)
---
## Swagger UI
<img width="915" height="749" alt="Screenshot 2026-04-06 230519" src="https://github.com/user-attachments/assets/431d6ba3-05c2-4693-89db-fe726438bf4e" />

## Schema
<img width="1346" height="369" alt="Screenshot 2026-04-06 230538" src="https://github.com/user-attachments/assets/0e10d77d-5083-4ac3-965e-b26a43a6f87f" />


---






   




 




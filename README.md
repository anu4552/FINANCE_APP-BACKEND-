# FINANCE_APP-BACKEND-
Assessment 

# 🚀 Finance Backend API

## 📌 Overview

This is a backend API built using FastAPI for managing financial records, user roles, and analytics.

## ⚙️ Tech Stack

* FastAPI
* MongoDB Atlas
* Python

## 🔐 Features

* User authentication (Admin, Analyst, Viewer)
* Role-based access control
* CRUD operations for financial records
* Filtering by date, category, type
* Secure API endpoints

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





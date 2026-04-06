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
 ## ADMIN 
 # 1.Register
 <img width="896" height="750" alt="Screenshot 2026-04-06 221136" src="https://github.com/user-attachments/assets/0cfc1627-ad22-494e-8343-33465f1ecaec" />

 # 2. Login 
 <img width="883" height="707" alt="Screenshot 2026-04-06 221221" src="https://github.com/user-attachments/assets/70faab1d-abcb-4fa3-86c8-dc9ce9f9506f" />

 # 3. Get Users
  <img width="1334" height="855" alt="Screenshot 2026-04-06 221318" src="https://github.com/user-attachments/assets/fea93829-5b11-40d2-9b62-6e8824b6db05" />

# 4. Create Records
   <img width="884" height="776" alt="Screenshot 2026-04-06 221443" src="https://github.com/user-attachments/assets/1849e837-a3f9-4e5f-9c32-636b43c67c8a" />

# 5. Read Records

   <img width="881" height="755" alt="Screenshot 2026-04-06 221541" src="https://github.com/user-attachments/assets/d1c3a824-c1d0-494f-8553-547fc962b267" />

# 6. Filter Records
<img width="879" height="674" alt="Screenshot 2026-04-06 221742" src="https://github.com/user-attachments/assets/962f7471-5d8d-448b-8bbf-9e88841706ea" />

# 7. Update Records
<img width="882" height="823" alt="Screenshot 2026-04-06 221910" src="https://github.com/user-attachments/assets/c6b7117b-7847-4539-a511-0e5a726e9816" />

# 8. Delete Records
<img width="877" height="504" alt="Screenshot 2026-04-06 221955" src="https://github.com/user-attachments/assets/4b89281a-f996-461c-bb55-f590075105ed" />

# 9. Summary (DASHBOARD)
<img width="1432" height="723" alt="Screenshot 2026-04-06 220237" src="https://github.com/user-attachments/assets/aa6433ad-b579-4b26-a430-006ad21e7fec" />

# 10. category-summary

<img width="1422" height="858" alt="Screenshot 2026-04-06 220304" src="https://github.com/user-attachments/assets/249d77b7-f3ec-49aa-a69b-78b5496c782d" />

# 11. recents 
<img width="1423" height="861" alt="Screenshot 2026-04-06 220401" src="https://github.com/user-attachments/assets/60b56388-d586-44d7-b30d-395411a6417d" />

# 12. Monthly-treands
<img width="1329" height="849" alt="Screenshot 2026-04-06 220449" src="https://github.com/user-attachments/assets/67e9605c-dcef-4c19-83ea-5387fed2c75b" />


---

## ANALYST

# 1.Register
 <img width="877" height="746" alt="Screenshot 2026-04-06 225040" src="https://github.com/user-attachments/assets/dff5d186-6370-4e56-ae62-a0b3211a6182" />


 # 2. Login 
 <img width="888" height="708" alt="Screenshot 2026-04-06 225134" src="https://github.com/user-attachments/assets/c26bfdf5-488f-4fea-8171-878b5ba3571c" />


 # 3. Read Records

   <img width="881" height="755" alt="Screenshot 2026-04-06 221541" src="https://github.com/user-attachments/assets/d1c3a824-c1d0-494f-8553-547fc962b267" />

# 4. Filter Records
<img width="879" height="674" alt="Screenshot 2026-04-06 221742" src="https://github.com/user-attachments/assets/962f7471-5d8d-448b-8bbf-9e88841706ea" />


# 5. Summary (DASHBOARD)
<img width="1432" height="723" alt="Screenshot 2026-04-06 220237" src="https://github.com/user-attachments/assets/aa6433ad-b579-4b26-a430-006ad21e7fec" />

# 6. category-summary

<img width="1422" height="858" alt="Screenshot 2026-04-06 220304" src="https://github.com/user-attachments/assets/249d77b7-f3ec-49aa-a69b-78b5496c782d" />

# 7. recents 
<img width="1423" height="861" alt="Screenshot 2026-04-06 220401" src="https://github.com/user-attachments/assets/60b56388-d586-44d7-b30d-395411a6417d" />

# 8. Monthly-treands
<img width="1329" height="849" alt="Screenshot 2026-04-06 220449" src="https://github.com/user-attachments/assets/67e9605c-dcef-4c19-83ea-5387fed2c75b" />

---
## VIEWER

# 1.Register
 <img width="882" height="728" alt="Screenshot 2026-04-06 224733" src="https://github.com/user-attachments/assets/6bd1ed3b-b367-4328-b835-94151fc9a5e3" />


 # 2. Login 
 <img width="884" height="707" alt="Screenshot 2026-04-06 224927" src="https://github.com/user-attachments/assets/121771c4-70b7-4bac-8a93-3f49f49e4872" />


# 3. Summary (DASHBOARD)
<img width="1432" height="723" alt="Screenshot 2026-04-06 220237" src="https://github.com/user-attachments/assets/aa6433ad-b579-4b26-a430-006ad21e7fec" />

# 4. category-summary

<img width="1422" height="858" alt="Screenshot 2026-04-06 220304" src="https://github.com/user-attachments/assets/249d77b7-f3ec-49aa-a69b-78b5496c782d" />

# 5. recents 
<img width="1423" height="861" alt="Screenshot 2026-04-06 220401" src="https://github.com/user-attachments/assets/60b56388-d586-44d7-b30d-395411a6417d" />

# 6. Monthly-treands
<img width="1329" height="849" alt="Screenshot 2026-04-06 220449" src="https://github.com/user-attachments/assets/67e9605c-dcef-4c19-83ea-5387fed2c75b" />





   




 




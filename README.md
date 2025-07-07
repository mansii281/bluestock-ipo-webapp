
# 📈 Bluestock IPO Web App

A Django-powered platform that displays live and upcoming IPOs in India, allowing users to view details, download PDFs, and explore IPO summaries.

---

## 🌐 Live Demo
🔗 [https://bluestock-ipo-webapp-production.up.railway.app](https://bluestock-ipo-webapp-production.up.railway.app)

---

## 🚀 Features
- 🔍 Browse upcoming IPOs with logos and PDF download links
- 📄 Admin Panel for CRUD operations on IPOs
- 📦 REST API using Django REST Framework with JWT Authentication
- 🖼️ Media file upload for logos (ImageField)
- 🧪 Tested using Postman (Alpha & Bug Testing Done)
- 📤 Deployed on Railway with PostgreSQL

---

## 🛠️ Tech Stack

| Layer       | Technology               |
|-------------|---------------------------|
| Backend     | Python, Django            |
| API         | Django REST Framework     |
| Auth        | JWT (djangorestframework-simplejwt) |
| Frontend    | HTML, CSS, Bootstrap 5    |
| Database    | PostgreSQL                |
| Deployment  | Railway                   |

---

## ⚙️ Local Development Setup

### 1. Clone the repo
```bash
git clone https://github.com/mansii281/bluestock-ipo-webapp
cd bluestock-ipo-webapp
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add `.env` file
Create `.env` in root folder:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=your-local-db-url
ALLOWED_HOSTS='*'
```

### 4. Run migrations & server
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 📂 API Endpoints (JWT Protected)

| Endpoint                 | Description                |
|--------------------------|----------------------------|
| `/api/token/`           | Get access & refresh token |
| `/api/token/refresh/`   | Refresh access token       |
| `/api/ipo/`             | Get all IPOs (GET/POST)    |
| `/api/ipo/<id>/`        | IPO detail (GET/PUT/DELETE)|

Tested in Postman ✅

---

## ⚙️ Deployment on Railway

1. Connect repo
2. Add `DEBUG`, `ALLOWED_HOSTS`, `DATABASE_URL`, `SECRET_KEY` in Railway Dashboard
3. Add Predeploy Command:
```bash
python manage.py makemigrations && python manage.py migrate && python manage.py collectstatic --noinput
```
4. Done ✅

---

## 📧 Author

**Mansi Sharma**  
📍 Greater Noida  


---

## ✅ Status

🟢 100% Complete  
🛠️ Alpha Testing + Bug Fixing done  
📤 Deployment Complete  
📦 Ready for submission

---


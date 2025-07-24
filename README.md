# 📝 Django Blog API (DRF + PostgreSQL)

A feature-rich, production-ready **Django REST Framework (DRF)** backend for a blogging platform. Built with clean modularity and JWT authentication.

---

## 🚀 Features

✅ Custom user model with email login
✅ JWT authentication using SimpleJWT
✅ Profile with avatar, phone number, and address
✅ Blog CRUD (Create, Read, Update, Delete)
✅ Publish/draft toggle with secure post visibility
✅ Search blog posts by title
✅ Pagination on blog listings
✅ Public user profile with list of their posts
✅ Admin panel for user and post management

---

## 🛠 Tech Stack

- Python 3.11+
- Django 4.x
- Django REST Framework (DRF)
- PostgreSQL
- SimpleJWT
- Pillow (for avatar support)
- Git + GitHub

---

## 📂 Project Structure

```plaintext
core/         # Django project settings
blog/         # App for users, blogs, views, serializers
media/        # Uploaded avatar images
requirements.txt  # Python dependencies
.env          # Environment config for DB and secrets (not committed)
```
---

## 🔐 API Endpoints

### 🔑 Auth
| Method | Endpoint            | Description           |
|--------|---------------------|-----------------------|
| POST   | `/register/`        | Register new user     |
| POST   | `/login/`           | Login, get JWT tokens |
| POST   | `/token/refresh/`   | Get new access token  |

---

### 👤 Profile
| Method | Endpoint    | Description               |
|--------|-------------|---------------------------|
| GET    | `/profile/` | Auth user's profile       |

---

### 📝 Blog Posts
| Method | Endpoint                  | Description                        |
|--------|---------------------------|------------------------------------|
| POST   | `/posts/create/`          | Create new blog post (auth)        |
| GET    | `/posts/`                 | List published posts (public)      |
| GET    | `/posts/<id>/`            | View a single published post       |
| PUT    | `/posts/<id>/edit/`       | Update post (author only)          |
| DELETE | `/posts/<id>/edit/`       | Delete post (author only)          |
| GET    | `/my-posts/`              | View all my posts incl. drafts     |

---

### 👥 Public User Profiles
| Method | Endpoint                        | Description                      |
|--------|----------------------------------|----------------------------------|
| GET    | `/users/<user_id>/`             | Public profile of a user         |
| GET    | `/users/<user_id>/posts/`       | Public blog posts by that user   |

---

### 🔍 Search & Pagination

| Feature    | Example URL                         | Description                        |
|------------|-------------------------------------|------------------------------------|
| Search     | `/posts/?search=python`             | Search published post titles       |
| Pagination | `/posts/?page=2`                    | Page through published posts       |

---

## 🧪 Setup Instructions

```bash
# 1. Clone this repo
git clone https://github.com/your-username/django-blog-api.git
cd django-blog-api

# 2. Create virtual environment
python -m venv drfvenv
source drfvenv/bin/activate  # Windows: drfvenv\Scripts\activate

# 3. Install requirements
pip install -r requirements.txt

# 4. Add .env file (DB and SECRET_KEY config)
# Example:
# SECRET_KEY=your-django-secret
# DEBUG=True
# DB_NAME=blogdb
# DB_USER=bloguser
# DB_PASSWORD=blogpass123
# DB_HOST=localhost
# DB_PORT=5432

# 5. Migrate and run server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
---

### ✅ Optional but Nice Ending

Add this below the setup instructions (outside the code block):


---

## 📸 Admin Panel

- URL: `/admin/`
- Use superuser credentials (`python manage.py createsuperuser`)

---

## 👨‍💻 Author

**Ashutosh Singh Tomar**
Learning Django & DRF step-by-step — building real projects from scratch.

---

## 💡 Next Steps

- 🔒 Logout with token blacklist
- 💬 Add comments & likes
- 🌐 Frontend using React
- 🚀 Deployment (Render, Railway, or Heroku)

---

## 📌 License

This project is for learning and demonstration purposes.

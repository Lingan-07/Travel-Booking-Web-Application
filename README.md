🚌 Travel Booking Application

A simple travel booking web application built with Django that allows users to:

Register, login, and manage profiles

View available travel options (Flight, Train, Bus)

Book and cancel tickets

View current and past bookings

🚀 Features

User authentication (register, login, logout, profile update)

Manage travel options (CRUD via Django admin)

Book tickets with seat validation

Cancel bookings & auto-return seats

Filter/search travel options by type, source, destination, date

Responsive frontend (Bootstrap)

🛠️ Tech Stack

Backend: Django (Python)

Frontend: Django Templates + Bootstrap

Database: SQLite (dev) / MySQL (production-ready)

Deployment: PythonAnywhere

⚙️ Installation (Local Setup)

Clone the repo

git clone https://github.com/Lingan-07/Travel-Booking-Web-Application
cd travelbooking


Create virtual environment & install dependencies

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

pip install -r requirements.txt


Database setup (SQLite by default)

python manage.py makemigrations
python manage.py migrate


Create superuser (admin access)

python manage.py createsuperuser


Seed sample travel data

python manage.py seed


Run server

python manage.py runserver


Visit 👉 http://127.0.0.1:8000/

🔑 Usage

/travel/ → View travel options

/travel/register/ → Create account

/accounts/login/ → Login

/travel/profile/ → Update profile

/travel/bookings/ → View/cancel bookings

/admin/ → Manage users, travel options, bookings


Deployment link & GitHub repo

✍️ Author: LINGAN C K
🔗 GitHub Repo: https://github.com/Lingan-07/Travel-Booking-Web-Application
🌍 Live Demo: [add deployment URL here]
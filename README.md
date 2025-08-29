🚌 Travel Booking Application

A simple travel booking web application built with Django that allows users to:

1.Register, login, and manage profiles

2.View available travel options (Flight, Train, Bus)

3.Book and cancel tickets

4.View current and past bookings



🚀 Features

1.User authentication (register, login, logout, profile update)

2.Manage travel options (CRUD via Django admin)

3.Book tickets with seat validation

4.Cancel bookings & auto-return seats

5.Filter/search travel options by type, source, destination, date

6.Responsive frontend (Bootstrap)



🛠️ Tech Stack

Backend: Django (Python)

Frontend: Django Templates + Bootstrap

Database: SQLite (dev) / MySQL (production-ready)

Deployment: PythonAnywhere



⚙️ Installation (Local Setup)

1.Clone the repo

git clone https://github.com/Lingan-07/Travel-Booking-Web-Application

cd travelbooking

2.Create virtual environment & install dependencies

python -m venv venv

venv\Scripts\activate   # On Windows

source venv/bin/activate  # On Linux/Mac

3.pip install -r requirements.txt

4.Database setup (SQLite by default)

python manage.py makemigrations

python manage.py migrate

5.Create superuser (admin access)

python manage.py createsuperuser

6.Seed sample travel data

python manage.py seed

7.Run server

python manage.py runserver

8.Visit 👉 http://127.0.0.1:8000/



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

🌍 Live Demo: https://lingan07.pythonanywhere.com/travel/

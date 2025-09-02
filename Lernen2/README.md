# Python
Python voll Kurs
Hier ist voll Kurs über python :
- KI
- Maschien Lerning
- Web Entwicklung

Code mit Python 3


# Hauptverzeichnis
mkdir my-django-angular-app
cd my-django-angular-app

# Backend erstellen
mkdir backend
cd backend

# Frontend erstellen (später)
cd ..
mkdir frontend

cd backend
python -m venv venv
venv\Scripts\activate
pip install django djangorestframework django-cors-headers

django-admin startproject config .
python manage.py startapp api

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
# Benutzername: admin
# Passwort: 12345

# RUN Backend  => python manage.py runserver


-----------------------------------------------------------------------

cd frontend

ng new my-app --routing=false --style=css --skip-git=true --skip-tests=true
cd my-app
npm install

# RUN Frontend  => ng serve

Frontend: http://localhost:4200

Backend API: http://localhost:8000/api/tasks/

Django Admin: http://localhost:8000/admin
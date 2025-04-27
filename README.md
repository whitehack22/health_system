# Health Information System (Django Project)

## Project Overview
This Health Information System is a Django-based web application that allows doctors to manage health programs and enroll clients into those programs. It also exposes client profile information via an API for easy integration with other systems.

### Key Features
- User Authentication (Login, Logout, Registration)
- Register New Clients
- View List of Clients
- Create, Edit, Delete, and View Health Programs (e.g., TB, Malaria, HIV programs)
- Enroll Clients into Programs
- REST API to expose Client Profile data (using Django REST Framework)

---

## Technologies Used
- Django 5.2
- Django REST Framework
- Bootstrap 5 (for UI Styling)
- MySQL (Database)

---

## Project Structure
```
health_system/
|└── core/                  # Core Django app
    |├── models.py          # Program and Client models
    |├── views.py           # Views for handling logic
    |├── urls.py            # URL configurations
    |├── serializers.py    # DRF Serializer for Client API
    |└── templates/         # HTML templates (home, program, client pages)
|├── manage.py
|└── requirements.txt
|└── README.md
```

---

## How to Set Up and Run the Project Locally

### 1. Ensure you have installed Python 3 and MySQL on your local machine

### 2. Clone the Repository
```bash
git clone https://github.com/whitehack22/health_system.git
cd health_system
```

### 3. Create and Activate Virtual Environment
```bash
python -m venv virt
# Activate on Windows
virt\Scripts\activate
# Activate on Mac/Linux
source virt/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Ensure you have setup the correct database credentials on your health_system/settings.py file
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'health_system',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'your_hostname',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### 7. Run the Development Server
```bash
python manage.py runserver
```
Visit: `http://127.0.0.1:8000/`

---

## Available Pages
- **Home Page**: Dashboard with actions (Register Client, View Clients, Create Program, View Programs)
- **Register New Client**
- **View Client List**
- **Create New Program**
- **View/Edit/Delete Programs**

## API Endpoint
- **GET Client Profile**:
```
http://127.0.0.1:8000/api/clients/<client_id>/
```

(You can test using Postman)

---

## How to Add a New Feature
- Create/Update your Model in `models.py`
- Create/Update your View in `views.py`
- Add the URL pattern in `urls.py`
- Create/Update your Template in `templates/`

---

## Future Improvements
- API Authentication with Token-Based Access
- Add search and filter options for clients and programs
- Upload and manage client-related documents

---

## Author
- Developed by Ryan Mugo Githaiga 💪

Feel free to contribute!



# Salon Booking System

A full-stack ready Salon Booking System backend built with Django, Django REST Framework, PostgreSQL, and JWT Authentication.

## Overview

The Salon Booking System allows customers to register, log in, and book salon services online. The system includes role-based access control, booking management, REST APIs, PostgreSQL integration, and production-ready configurations.

## Features

### Authentication & Authorization

* Custom User Model
* User Registration
* User Login & Logout
* Role-Based Access Control
* Customer Group Assignment
* JWT Authentication
* Token-Based Authentication

### Booking Management

* Create Booking
* View Bookings
* Update Booking
* Delete Booking
* Customer Dashboard
* Manager Dashboard

### Validation

* Prevent Past Date Bookings
* Restrict Booking Time to Salon Working Hours
* Prevent Duplicate Booking Slots

### REST APIs

* Django REST Framework
* ModelViewSet Implementation
* CRUD APIs
* API Authentication
* Pagination Ready
* Filtering Ready

### Database

* PostgreSQL Integration
* Django ORM
* Database Migrations

### Production Ready

* Environment Variables (.env)
* CORS Configuration
* Swagger API Documentation
* Requirements File
* Git Ignore Configuration

---

## Tech Stack

### Backend

* Python
* Django
* Django REST Framework

### Database

* PostgreSQL

### Authentication

* JWT Authentication
* DRF Token Authentication

### Documentation

* drf-spectacular (Swagger/OpenAPI)

---

## Project Structure

```text
salon_project/
│
├── accounts/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
│
├── saloon/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│
├── static/
│
├── manage.py
├── requirements.txt
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/salon-booking-system.git

cd salon-booking-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE salon_db;
```

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DB_NAME=salon_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

---

## Apply Migrations

```bash
python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Run Server

```bash
python manage.py runserver
```

Application URL:

```text
http://127.0.0.1:8000/
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/api/docs/
```

OpenAPI Schema:

```text
http://127.0.0.1:8000/api/schema/
```

---

## Authentication Endpoints

### JWT Login

```http
POST /api/token/
```

Request:

```json
{
    "username": "user",
    "password": "password"
}
```

Response:

```json
{
    "refresh": "token",
    "access": "token"
}
```

### Refresh Token

```http
POST /api/token/refresh/
```

---

## Booking API Endpoints

### List Bookings

```http
GET /api/bookings/
```

### Create Booking

```http
POST /api/bookings/
```

### Update Booking

```http
PUT /api/bookings/{id}/
```

### Delete Booking

```http
DELETE /api/bookings/{id}/
```

---

## Future Enhancements

* React Frontend Integration
* Online Payments
* Email Notifications
* Appointment Reminders
* Service Management
* Staff Management
* Analytics Dashboard
* Docker Deployment
* Cloud Deployment (AWS / Render)

---

## Learning Outcomes

This project demonstrates practical experience with:

* Django Fundamentals
* Django ORM
* Forms and CRUD Operations
* Authentication & Authorization
* Django REST Framework
* JWT Authentication
* PostgreSQL
* API Development
* Environment Variables
* Swagger Documentation
* Production Ready Backend Development

---

## Author

Vishnu R

Backend Developer | Django Developer | Python Developer

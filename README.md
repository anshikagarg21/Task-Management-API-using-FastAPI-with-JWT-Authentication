# Task Management API

A backend Task Management API built using FastAPI with JWT-based authentication.

## Features
- User registration and login
- JWT authentication
- Role-based access control
- Task CRUD APIs
- SQLite database

## Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload

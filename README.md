E-Commerce Project

Description:
This is a full-featured E-Commerce web application developed using Django and Django REST Framework (DRF). It allows users to browse products, add them to cart, place orders, and manage their accounts. Admins can manage products, categories, and users through the Django admin panel.

Features:

User authentication and authorization (JWT based).

Product listing, filtering, and searching.

Shopping cart and order placement system.

Admin dashboard to manage users, products, and categories.

RESTful APIs for all major functionalities.

Technologies Used:

Backend: Django, Django REST Framework

Database: PostgreSQL

Authentication: JWT (Simple JWT)

Frontend: Django Templates (for admin and basic UI)

Deployment: Localhost / can be deployed on any cloud platform

Installation / Setup:

Clone the repository:

git clone https://github.com/Sharatpsd/E-Commerce-Project-Backend-Django.git


Create and activate virtual environment:

python -m venv venv
venv\Scripts\activate   # For Windows


Install dependencies:

pip install -r requirements.txt


Setup .env file with database credentials.

Run migrations:

python manage.py makemigrations
python manage.py migrate


Create superuser for admin panel:

python manage.py createsuperuser


Run the server:

python manage.py runserver


Access the admin panel: http://127.0.0.1:8000/admin/

Usage:

Users can register, login, browse products, add to cart, and place orders.

Admin can manage products, categories, and users from the admin panel.

APIs are available for frontend integration or mobile apps.

Deployment:

Project can be deployed on Heroku, AWS, or any VPS.

Configured to use PostgreSQL as production database.

Author:
Sharat Acharja Mugdho

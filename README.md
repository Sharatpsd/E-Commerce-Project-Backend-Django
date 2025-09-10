# E-Commerce Web Application

## Overview
This is a full-featured **E-Commerce web application** developed using **Django, Django REST Framework (DRF), and PostgreSQL**. It allows users to browse products, manage shopping carts, place orders, and handle payments. The project is designed for scalability, real-world usability, and smooth frontend-backend integration.

---

## Features

### User Features
- User registration and login with **JWT Authentication**
- Profile management (update personal info)
- Browse and search products by category
- Add products to **shopping cart**
- Place orders and view order history
- Secure checkout with payment simulation

### Admin Features
- Admin panel to manage products, categories, and orders
- Manage users and roles (admin, customer)
- Full control over product inventory and pricing

### Technical Features
- Backend built with **Django & Django REST Framework**
- RESTful APIs for frontend consumption
- Database: **PostgreSQL**
- JWT authentication for secure API access
- Deployed locally (can be deployed on cloud platforms like Heroku or AWS)
- Responsive and modern admin interface

---

## Tech Stack
- **Backend:** Python, Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Frontend (Admin Panel):** Django Admin
- **Deployment (Optional):** Heroku / AWS / Localhost

---

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/Sharatpsd/E-Commerce-Project-Backend-Django.git
cd E-Commerce-Project
Create and activate virtual environment

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Install dependencies

bash
Copy code
pip install -r requirements.txt
Set up environment variables
Create a .env file in the root directory and add:

ini
Copy code
SECRET_KEY=<your-secret-key>
DEBUG=True
DB_NAME=<your-db-name>
DB_USER=<your-db-user>
DB_PASSWORD=<your-db-password>
DB_HOST=127.0.0.1
DB_PORT=5432
Apply migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create superuser

bash
Copy code
python manage.py createsuperuser
Run the server

bash
Copy code
python manage.py runserver
Visit http://127.0.0.1:8000/admin/ for admin panel.

API Endpoints
/api/products/ - List all products

/api/products/<id>/ - Product details

/api/cart/ - User's cart management

/api/orders/ - Place and view orders

/api/auth/ - Registration & login endpoints

For full API documentation, see /docs/ or Postman collection (if included).

Deployment
This project can be deployed on Heroku, AWS, or any cloud server.

Use PostgreSQL in production.

Set environment variables securely and enable DEBUG=False in production.

Contributing
Fork the repository

Create your branch (git checkout -b feature/your-feature)

Commit your changes (git commit -m 'Add feature')

Push to branch (git push origin feature/your-feature)

Open a Pull Request

License
This project is open-source and available under the MIT License.

Author
Sharat Acharja Mugdho
BSc in Computer Science & Engineering, Green University of Bangladesh
Email: <your-email>

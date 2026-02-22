DXSure CRM - Project Documentation

Overview
A full-stack Customer Relationship Management (CRM) web application built to streamline client tracking, employee management, and business financials.

Key Features

Interactive Dashboard: Real-time metrics tracking total clients, total employees, total company revenue, payroll, and dynamic net profit/loss calculations.

Client Management: Full CRUD (Create, Read, Update, Delete) functionality to manage client details, sales funnel status (Lead, Active, Past), industry, and generated revenue.

Employee Directory: Complete internal database tracking roles, departments, hire dates, and salaries with full CRUD capabilities.

Responsive UI: Clean, modern, and mobile-friendly interface.

Technology Stack

Backend: Python, Django

Database: MySQL (via XAMPP)

Frontend: HTML, CSS, Bootstrap 5

Local Setup & Installation Instructions

1. Clone the repository:
Open your command prompt and run:
git clone https://github.com/YOUR-USERNAME/dxsure-crm.git
cd dxsure-crm

2. Set up a virtual environment:
Ensure your dependencies are isolated by creating a virtual environment:
python -m venv venv
venv\Scripts\activate

3. Install dependencies:
Install the required Python packages:
pip install django mysqlclient

4. Database Configuration:

Start the XAMPP Control Panel and ensure the MySQL module is running.

Open phpMyAdmin and create a new database named dxsure_db.

5. Apply Database Migrations:
Sync the Django models with your MySQL database:
python manage.py makemigrations
python manage.py migrate

6. Run the Development Server:
Launch the application locally:
python manage.py runserver

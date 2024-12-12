# Employee Management System

## Table of Contents
1. [Overview](#overview)
2. [Approach & Implementation](#approach-implementation)
3. [Setup Instructions](#setup-instructions)
4. [Task Checklist](#task-checklist)
5. [Security Measures](#security-measures)
6. [API Documentation](#api-documentation)

---

## Overview

The **Employee Management System** is designed to help organizations manage their **companies**, **departments**, and **employees** efficiently. The system provides features for:

- Managing company profiles
- Structuring and managing departments
- Managing employee profiles, performance, and data
- Role-based access to different system features

This system also incorporates **role-based access control** to ensure that only authorized personnel can perform sensitive operations like managing employees and modifying company data.

---

## Approach & Implementation

The system is built using a **Vue.js** front-end with a **Django** back-end. The application leverages the following technologies:

- **Vue.js** (for the front-end)
  - Used to create a dynamic, reactive UI to interact with the backend APIs.
  - **Vue Router** is used for navigation between pages.
  - **Pinia** is used for state management.
  
- **Django REST Framework** (for the back-end)
  - Handles API endpoints for managing employees, departments, and companies.
  - Role-based access is implemented using Django permissions and authentication.

### Key Features Implemented:
1. **Company Management**:
   - Add, update, and delete company details.
   - View a list of all companies.
   - View a specific company.

2. **Department Management**:
   - Create and assign employees to departments.
   - Assign departments to companies.
   - View all departments within a company.
   - View a specific department.

3. **Employee Management**:
   - CRUD (Create, Read, Update, Delete) operations for employee profiles.
   - Assign employees to departments which associated to specific company and manage their roles.
   - View all employees within a department.
   - View a specific employee data.

4. **Role-Based Access Control**:
   - **Admin**: Full access to manage companies, departments, and employees.
   - **Manager**: Can view and manage data.
   - **Employee**: Can only view data.

5. **Security Measures**:
   - Authentication via **JWT (JSON Web Tokens)**.
   - Authorization using Django's **permissions** and role-based access control.
   - Secure handling of sensitive information, such as employee details and company data.

---

## Setup Instructions

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** and **npm** (for front-end)
  - Download and install from: [https://nodejs.org/](https://nodejs.org/)

- **Python** and **Django** (for back-end)
  - Install Python from: [https://www.python.org/](https://www.python.org/)
  - Install Django via pip:
    ```bash
    pip install django djangorestframework
    ```

- **Vue.js** (for the front-end)
  - Install Vue CLI if you don't have it:
    ```bash
    npm install -g @vue/cli
    ```

### Step-by-Step Installation

#### 1. **Set up the backend (Django)**

1. Clone the repository or navigate to your backend folder:
   ```bash
   git clone https://github.com/yourusername/brainwise.git
   cd brainwise
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations to set up the database schema:
   ```bash
   python manage.py migrate
   python manage.py makemigrations
   ```
4. Create a superuser to access the Django admin panel:
   ```bash
   python manage.py createsuperuser
   ```
5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
6. The back-end API will be available at http://127.0.0.1:8000/.


#### 2. **Set up the frontend (Vue.js)**

1. Clone the repository or navigate to your frontend folder:
   ```bash
   git clone https://github.com/yourusername/frontend.git
   cd frontend
   ```
2. Install the required Node.js dependencies:
   ```bash
   npm install
   ```
3. Configure the base API URL in the frontend project:
   - Open the configuration file (e.g., src/config.js or src/store/api.js) and set the API base URL to match the back-end server address (http://127.0.0.1:8000/).
4. Start the Vue.js development server:
   ```bash
   npm run serve
   ```
5. Open your browser and navigate to http://localhost:8080/ to access the application.

## Task Checklist

- [x] **Company Management**: CRUD operations for companies.
- [x] **Department Management**: CRUD operations for departments and assigning employees.
- [x] **Employee Management**: CRUD operations for employees.
- [x] **Role-Based Access Control**: Implement admin, manager, and employee roles.
- [x] **API Endpoints**: Define and document the API endpoints for interaction with the front-end.
- [x] **Authentication**: Implement JWT token-based authentication.
- [x] **Authorization**: Implement role-based access control using Django permissions.
- [x] **Front-end UI**: Implement a user-friendly UI using Vue.js for all features.
- [x] **Back-end API**: Implement RESTful APIs for managing companies, departments, and employees.

# Security Measures

## JWT Authentication
- Tokens are used to authenticate users.
- Expiration and refresh mechanisms ensure secure access.

## Role-Based Access Control
- **Admins**: Unrestricted access to the entire system.
- **Managers**: Can view and manage data.
- **Employees**: Can only view data.

## Data Protection
- Sensitive information is stored securely.
- All API communications are protected using HTTPS.

## CSRF Protection
- Cross-Site Request Forgery tokens are used to prevent unauthorized actions.

# Accessing Full API Documentation

Use tools like **Postman** or **Swagger** to:  
- Test API functionality.  
- View detailed documentation for all API endpoints.  
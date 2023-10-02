# CRUD_goods Project

CRUD_goods is a Django-based web application for managing and displaying product information. This project includes
features such as user registration, product management, and API endpoints for interacting with product data.

## Features

- User Registration: Users can sign up for accounts to access the system.
- Product Management: Add, view, edit, and delete product information, including name, category, price, and more.
- Product Categories: Organize products into categories.
- API Endpoints: Access product and category data via RESTful API endpoints.
- User Authentication: Secure user authentication using Django's authentication system.
- Token-Based Authentication: Authenticate API requests using token-based authentication.

## Getting Started

These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following requirements installed:

- Python (3.x recommended)
- Django
- Django Rest Framework
- Other project-specific dependencies (specified in `requirements.txt`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eduardzapadinsky/CRUD_goods.git
   ```

2. Navigate to the project directory:

   ```bash
   cd CRUD_goods
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Create a superuser account (for admin access):

   ```bash
   python manage.py createsuperuser
   ```

8. Start the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

- Visit the admin interface to manage products, categories, and user accounts.
- Access the API endpoints at `http://localhost:8000/api/` to interact with product and category data via API calls.




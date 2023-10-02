# CRUD Goods

CRUD Goods is a Django-based web application for managing product listings with support for nested descriptions.

## Features

- Create, read, update, and delete products.
- Organize products by categories.
- Filter products by various criteria such as "Offer of the Month," "Availability," and "Pickup."

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eduardzapadinsky/CRUD_goods.git
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Migrate the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

- `/api/user/signup/`: Register a new user.
- `/api/user/auth/`: Obtain authentication tokens by providing valid credentials.
- `/api/user/token_refresh/`: Refresh authentication tokens.
- `/api/goods/categories/`: List and create product categories.
- `/api/goods/categories/<int:pk>/`: Retrieve, update, and delete a specific category.
- `/api/goods/goods/`: List and create products with support for nested descriptions.
- `/api/goods/goods/<int:pk>/`: Retrieve, update, and delete a specific product.
- `/api/goods/goods/category/<str:category>/`: List products by category.
- `/api/goods/goods/offer-of-the-month/`: List products with "Offer of the Month."
- `/api/goods/goods/availability/`: List available products.
- `/api/goods/goods/pickup/`: List products available for pickup.


## Usage

- Access the API endpoints at `http://localhost:8000/api/` to interact with product and category data via API calls.

### Create a New Product

To create a new product, send a POST request to the `/api/goods/goods/` endpoint with the following JSON data as the request body:

```json
{
    "category": {
        "category_name": "Cats"
    },
    "name": "Cat 1",
    "photo": "https://loremflickr.com/320/240/",
    "offer_of_the_month": true,
    "availability": false,
    "pickup": true,
    "price": "434.00",
    "description": [
        "Description 01",
        "Description 02"
    ]
}
```






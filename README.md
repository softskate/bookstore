# Bookstore Management System

This project is a simple Bookstore Management System built with Django. It allows you to perform CRUD (Create, Read, Update, Delete) operations on books, authors, and categories. Each book can have multiple authors and belong to one category.

## Features

- **Books**: Create, Read, Update, and Delete books.
- **Authors**: Create, Read, Update, and Delete authors.
- **Categories**: Create, Read, Update, and Delete categories.
- **ORM**: Uses Django ORM for database operations.
- **Web Interface**: Simple web interface using Django Templates.
- **Web API**: RESTful API for books, authors, and categories.

## Technologies Used

- **Backend**: Django
- **Database**: SQLite (default with Django, can be changed to PostgreSQL, MySQL, etc.)
- **Frontend**: Django Templates

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/bookstore.git
    cd bookstore
    ```

2. **Create a virtual environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations**

    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**

    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**

    ```bash
    python manage.py runserver
    ```

8. **Access the application**

    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Managing Books

- Go to `http://127.0.0.1:8000/books/` to view the list of books.
- Click on "Add Book" to create a new book.
- Click on "Edit" to update an existing book.
- Click on "Delete" to remove a book.

### Managing Authors

- Go to `http://127.0.0.1:8000/authors/` to view the list of authors.
- Click on "Add Author" to create a new author.
- Click on "Edit" to update an existing author.
- Click on "Delete" to remove an author.

### Managing Categories

- Go to `http://127.0.0.1:8000/categories/` to view the list of categories.
- Click on "Add Category" to create a new category.
- Click on "Edit" to update an existing category.
- Click on "Delete" to remove a category.

## Web API

The application also provides a RESTful API for interacting with books, authors, and categories. The following endpoints are available:

### Books

- **GET /api/books/**: Retrieve a list of books.
- **POST /api/books/**: Create a new book.
- **GET /api/books/{id}/**: Retrieve details of a specific book.
- **PUT /api/books/{id}/**: Update a specific book.
- **DELETE /api/books/{id}/**: Delete a specific book.

### Authors

- **GET /api/authors/**: Retrieve a list of authors.
- **POST /api/authors/**: Create a new author.
- **GET /api/authors/{id}/**: Retrieve details of a specific author.
- **PUT /api/authors/{id}/**: Update a specific author.
- **DELETE /api/authors/{id}/**: Delete a specific author.

### Categories

- **GET /api/categories/**: Retrieve a list of categories.
- **POST /api/categories/**: Create a new category.
- **GET /api/categories/{id}/**: Retrieve details of a specific category.
- **PUT /api/categories/{id}/**: Update a specific category.
- **DELETE /api/categories/{id}/**: Delete a specific category.

## Project Structure

bookstore/
├── bookstore/
│ ├── init.py
│ ├── settings.py
│ ├── urls.py
│ ├── wsgi.py
│ └── asgi.py
├── store/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ ├── api_views.py # API views
│ ├── serializers.py # Serializers for API
│ ├── templates/
│ │ └── store/
│ │ ├── base.html
│ │ ├── book_list.html
│ │ ├── book_form.html
│ │ ├── author_list.html
│ │ ├── author_form.html
│ │ ├── category_list.html
│ │ ├── category_form.html
│ │ └── book_confirm_delete.html
│ │ └── author_confirm_delete.html
│ │ └── category_confirm_delete.html
└── manage.py

python
Copy code

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
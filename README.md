# Online Library - Book Review System

A comprehensive Django-based web application for managing an online library with book reviews, user authentication, and category management.

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [API Endpoints](#api-endpoints)
- [Admin Panel](#admin-panel)
- [License](#license)

## ✨ Features

### User Management
- **User Registration**: New users can create accounts with email, first name, and last name
- **User Authentication**: Secure login/logout functionality
- **Profile Management**: Users can manage their reviews and account information

### Book Management
- **Book Catalog**: Browse all available books in the library
- **Book Details**: View detailed information about each book including:
  - Title, Author, Category
  - Description and Cover Image
  - Average Rating
  - Total Number of Reviews
- **Search Functionality**: Search books by title or author
- **Category Filtering**: Filter books by category

### Review System
- **Add Reviews**: Authenticated users can write reviews for books
- **Rating System**: Rate books from 1 to 5 stars
- **Edit Reviews**: Users can edit their own reviews
- **Delete Reviews**: Users can delete their own reviews
- **One Review Per User**: Each user can only submit one review per book
- **Review Display**: View all reviews for a specific book with ratings and comments

### Admin Features
- **Category Management**: Create and manage book categories
- **Book Management**: Add, edit, and delete books
- **Review Moderation**: View and manage all user reviews
- **User Management**: Manage user accounts

## 🛠 Technologies Used

- **Backend Framework**: Django 5.2.7
- **Database**: SQLite3 (Development)
- **Frontend**: HTML, CSS (Bootstrap)
- **Image Handling**: Pillow
- **Authentication**: Django's built-in authentication system
- **Python Version**: Python 3.x

## 📁 Project Structure

```
online_library/
├── online_library/          # Project configuration
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL configuration
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
├── library/                # Main application
│   ├── migrations/         # Database migrations
│   ├── templates/          # HTML templates
│   │   └── books/         # Book-related templates
│   ├── __init__.py
│   ├── admin.py           # Admin panel configuration
│   ├── apps.py            # App configuration
│   ├── forms.py           # Django forms
│   ├── models.py          # Database models
│   ├── urls.py            # App URL patterns
│   ├── views.py           # View functions
│   └── tests.py           # Unit tests
├── media/                 # User-uploaded files
│   └── book_covers/       # Book cover images
├── static/                # Static files (CSS, JS, images)
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script
```

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Create and activate virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. **Install required packages**
   ```bash
   pip install django==5.2.7
   pip install pillow
   ```

3. **Run the development server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/


## 📖 Usage

### For Regular Users

1. **Register an Account**
   - Navigate to the registration page
   - Fill in username, email, first name, last name, and password
   - Submit the form to create your account

2. **Browse Books**
   - View all available books on the homepage
   - Use the search bar to find books by title or author
   - Filter books by category

3. **View Book Details**
   - Click on any book to view its details
   - See the book's description, author, category, and cover image
   - View average rating and all reviews

4. **Write a Review**
   - Login to your account
   - Navigate to a book's detail page
   - Click "Add Review"
   - Select a rating (1-5 stars) and write your comment
   - Submit the review

5. **Manage Your Reviews**
   - Edit your reviews by clicking the "Edit" button
   - Delete your reviews by clicking the "Delete" button

### For Administrators

1. **Access Admin Panel**
   - Navigate to http://127.0.0.1:8000/admin/
   - Login with your superuser credentials

2. **Manage Categories**
   - Add new book categories
   - Edit or delete existing categories

3. **Manage Books**
   - Add new books with title, author, category, description, and cover image
   - Edit existing book information
   - Delete books

4. **Moderate Reviews**
   - View all user reviews
   - Delete inappropriate reviews if necessary

## 🗄️ Models

### Category Model
```python
- name: CharField (max_length=100, unique)
- description: TextField (optional)
```

### Book Model
```python
- title: CharField (max_length=200)
- author: CharField (max_length=200)
- category: ForeignKey to Category
- description: TextField
- cover_image: ImageField (optional)
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)

Methods:
- average_rating(): Returns average rating from all reviews
- total_reviews(): Returns total number of reviews
```

### Review Model
```python
- book: ForeignKey to Book
- user: ForeignKey to User
- rating: IntegerField (1-5)
- comment: TextField
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)

Constraints:
- unique_together: ['book', 'user'] (one review per user per book)
```

## 🔗 API Endpoints

### Authentication
- `GET/POST /register/` - User registration
- `GET/POST /login/` - User login
- `POST /logout/` - User logout

### Books
- `GET /` - List all books (with search and filter)
- `GET /book/<int:pk>/` - Book detail page

### Reviews
- `GET/POST /book/<int:pk>/review/add/` - Add a review (requires login)
- `GET/POST /review/<int:pk>/edit/` - Edit a review (requires login)
- `GET/POST /review/<int:pk>/delete/` - Delete a review (requires login)

### Admin
- `GET /admin/` - Django admin panel

## 👨‍💼 Admin Panel

The admin panel provides comprehensive management features:

### Category Admin
- List view with name and description
- Search by category name

### Book Admin
- List view showing title, author, category, creation date, average rating, and total reviews
- Filter by category and creation date
- Search by title and author
- Organized fieldsets for better UX

### Review Admin
- List view showing book, user, rating, and creation date
- Filter by rating and creation date
- Search by book title, username, and comment content

## 📝 License

This project is developed by **Jijanur Rahman** as part of personal practice for a Django full-stack development journey.


## 📧 Contact

For any questions or suggestions, please contact:
- **Developer**: [Jijanur Rahman](https://jijanurrahman.netlify.app)
- **Project**: Online Library (Book Review System)

---

**Note**: This is a development version. Please ensure proper security configurations before deploying to production.

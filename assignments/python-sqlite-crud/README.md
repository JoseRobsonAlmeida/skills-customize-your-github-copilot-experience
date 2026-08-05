# 📘 Assignment: Python SQLite CRUD

## 🎯 Objective

Build a school library manager in Python using SQLite to practice data persistence, SQL queries, and CRUD operations with input validation.

## 📝 Tasks

### 🛠️ Create the Database and Schema

#### Descrição
Set up a local SQLite database and create the table used to store the library books.

#### Requisitos
O programa concluído deve:

- Create a SQLite database file named `library.db`.
- Create a table `books` with columns: `id` (INTEGER PRIMARY KEY AUTOINCREMENT), `title` (TEXT NOT NULL), `author` (TEXT NOT NULL), `year` (INTEGER), and `available` (INTEGER NOT NULL DEFAULT 1).
- Avoid duplicating schema creation errors by using `CREATE TABLE IF NOT EXISTS`.
- Provide a function `init_db()` that can be safely run multiple times.

### 🛠️ Implement Full CRUD Operations

#### Descrição
Implement functions to create, read, update, and delete books in the database.

#### Requisitos
O programa concluído deve:

- Implement `add_book(title, author, year, available=True)` to insert a new book.
- Implement `list_books()` to return all books ordered by `id`.
- Implement `update_book(book_id, title=None, author=None, year=None, available=None)` to update existing data only for fields provided.
- Implement `delete_book(book_id)` and return whether a row was actually deleted.
- Use parameterized SQL queries (`?`) in every query to prevent SQL injection.

### 🛠️ Add Search and Validation

#### Descrição
Improve usability by supporting simple filters and validating data before writing to the database.

#### Requisitos
O programa concluído deve:

- Implement `find_books_by_author(author_name)` using a `LIKE` query.
- Validate that `title` and `author` are not empty strings.
- Validate that `year` is between 1450 and the current year.
- Validate that `available` is stored as `0` or `1` in the database.
- Demonstrate usage with a short CLI menu or a `main()` function that runs sample operations.

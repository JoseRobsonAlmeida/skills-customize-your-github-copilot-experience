import sqlite3
from datetime import datetime

DB_PATH = "library.db"


def get_connection():
    """Create and return a SQLite connection."""
    return sqlite3.connect(DB_PATH)


def init_db():
    """Create the books table if it does not exist."""
    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 1: Create books table with the required schema
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INTEGER,
                available INTEGER NOT NULL DEFAULT 1
            )
            """
        )
        conn.commit()


def _validate_book_data(title=None, author=None, year=None, available=None):
    """Validate user-provided fields before database writes."""
    if title is not None and not title.strip():
        raise ValueError("title cannot be empty")

    if author is not None and not author.strip():
        raise ValueError("author cannot be empty")

    if year is not None:
        current_year = datetime.now().year
        if year < 1450 or year > current_year:
            raise ValueError(f"year must be between 1450 and {current_year}")

    if available is not None and available not in (0, 1, True, False):
        raise ValueError("available must be 0 or 1")


def add_book(title, author, year, available=True):
    """Insert a new book and return its generated id."""
    _validate_book_data(title=title, author=author, year=year, available=available)
    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 2: Insert a new row into books using parameterized SQL
        cursor.execute(
            "INSERT INTO books (title, author, year, available) VALUES (?, ?, ?, ?)",
            (title.strip(), author.strip(), year, int(bool(available))),
        )
        conn.commit()
        return cursor.lastrowid


def list_books():
    """Return all books ordered by id."""
    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 2: Fetch all rows ordered by id
        cursor.execute("SELECT id, title, author, year, available FROM books ORDER BY id")
        return cursor.fetchall()


def update_book(book_id, title=None, author=None, year=None, available=None):
    """Update only the provided fields. Return True if row was updated."""
    _validate_book_data(title=title, author=author, year=year, available=available)

    fields = []
    values = []

    if title is not None:
        fields.append("title = ?")
        values.append(title.strip())
    if author is not None:
        fields.append("author = ?")
        values.append(author.strip())
    if year is not None:
        fields.append("year = ?")
        values.append(year)
    if available is not None:
        fields.append("available = ?")
        values.append(int(bool(available)))

    if not fields:
        return False

    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 2: Complete update query and execute it
        query = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
        values.append(book_id)
        cursor.execute(query, values)
        conn.commit()
        return cursor.rowcount > 0


def delete_book(book_id):
    """Delete a book by id. Return True if row was deleted."""
    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 2: Delete row by id
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        return cursor.rowcount > 0


def find_books_by_author(author_name):
    """Search books by partial author name (case-insensitive)."""
    if not author_name.strip():
        raise ValueError("author_name cannot be empty")

    with get_connection() as conn:
        cursor = conn.cursor()
        # TODO Task 3: Use LIKE filter for author search
        cursor.execute(
            "SELECT id, title, author, year, available FROM books WHERE author LIKE ? ORDER BY id",
            (f"%{author_name.strip()}%",),
        )
        return cursor.fetchall()


def main():
    """Simple demo flow for quick manual testing."""
    init_db()

    # TODO Task 3: Replace this demo with your own test flow
    book_id = add_book("Clean Code", "Robert C. Martin", 2008, True)
    print("Inserted book id:", book_id)

    print("All books:")
    for row in list_books():
        print(row)

    print("Books by author 'Martin':")
    for row in find_books_by_author("Martin"):
        print(row)


if __name__ == "__main__":
    main()

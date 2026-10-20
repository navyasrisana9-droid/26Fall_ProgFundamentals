import sqlite3

# Connect to database
conn = sqlite3.connect("library.db")
cur = conn.cursor()

# Remove existing table
cur.execute("DROP TABLE IF EXISTS books")

# Create books table
cur.execute("""
CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    genre TEXT,
    copies INTEGER,
    rating INTEGER
)
""")

# Add one book with a single INSERT statement
cur.execute("""
INSERT INTO books
VALUES
(1, 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Fiction', 3, 5)
""")

# Add remaining books using executemany and placeholders
books = [
    (2, 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction', 4, 5),
    (3, '1984', 'George Orwell', 1949, 'Fiction', 2, 4),
    (4, 'A Brief History of Time', 'Stephen Hawking', 1988, 'Science', 5, None),
    (5, 'The Selfish Gene', 'Richard Dawkins', 1976, 'Science', 3, 5),
    (6, 'The Diary of a Young Girl', 'Anne Frank', 1947, 'History', 2, None),
    (7, 'The Da Vinci Code', 'Dan Brown', 2003, 'Mystery', 6, 4),
    (8, 'Sapiens', 'Yuval Noah Harari', 2011, 'History', 4, 5)
]

cur.executemany(
    "INSERT INTO books VALUES (?, ?, ?, ?, ?, ?, ?)",
    books
)

conn.commit()

# 3. Books after 1990
print("\nBooks Published After 1990:")
for row in cur.execute(
    "SELECT title, author FROM books WHERE year > 1990"
):
    print(row)

# 4. Fiction books with more than 2 copies
print("\nFiction Books With More Than 2 Copies:")
for row in cur.execute(
    "SELECT title FROM books WHERE genre='Fiction' AND copies > 2"
):
    print(row[0])

# 5. Published before 1900 OR rated 5
print("\nBooks Published Before 1900 OR Rated 5:")
for row in cur.execute(
    "SELECT title FROM books WHERE year < 1900 OR rating = 5"
):
    print(row[0])

# 6. NOT Mystery
print("\nBooks That Are NOT Mystery:")
for row in cur.execute(
    "SELECT title FROM books WHERE NOT genre='Mystery'"
):
    print(row[0])

# 7. Science or History genre
print("\nScience or History Books:")
for row in cur.execute(
    "SELECT title FROM books WHERE genre IN ('Science', 'History')"
):
    print(row[0])

# 8. LIKE query
letter = input("\nEnter a letter: ")

print(f"\nAuthors Starting With '{letter}':")
for row in cur.execute(
    "SELECT author FROM books WHERE author LIKE ?",
    (letter + "%",)
):
    print(row[0])

# 9. No rating
print("\nBooks With No Rating:")
for row in cur.execute(
    "SELECT title FROM books WHERE rating IS NULL"
):
    print(row[0])

# Close connection
conn.close()

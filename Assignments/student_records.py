import sqlite3

# Connect to database
conn = sqlite3.connect("StudentRecords.db")
cur = conn.cursor()

# Remove existing table
cur.execute("DROP TABLE IF EXISTS StudentRecords")

# Create table
cur.execute("""
CREATE TABLE StudentRecords (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Major TEXT
)
""")

# Add 5 students
students = [
    (1, "Emma", 19, "Biology"),
    (2, "John", 20, "Computer Science"),
    (3, "Sophia", 18, "Nursing"),
    (4, "Liam", 21, "History"),
    (5, "Olivia", 19, "Business")
]

cur.executemany(
    "INSERT INTO StudentRecords VALUES (?, ?, ?, ?)",
    students
)

# Print student information
print("\nCurrent Students:")
cur.execute("SELECT Name, Age, Major FROM StudentRecords")

for student in cur.fetchall():
    print(student)

# Ask yes/no question
while True:
    answer = input(
        "\nDo you want to add a new student? (yes/no): "
    ).strip().lower()

    if answer in ["yes", "no"]:
        break

    print("Please enter yes or no.")

# Add student if yes
if answer == "yes":

    while True:
        name = input("Enter student's name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    while True:
        try:
            age = int(input("Enter student's age: "))
            break
        except ValueError:
            print("Age must be a whole number.")

    while True:
        major = input("Enter student's major: ").strip()
        if major:
            break
        print("Major cannot be empty.")

    # Generate unused ID
    cur.execute("SELECT MAX(ID) FROM StudentRecords")
    new_id = cur.fetchone()[0] + 1

    # Insert with placeholders
    cur.execute(
        """
        INSERT INTO StudentRecords
        (ID, Name, Age, Major)
        VALUES (?, ?, ?, ?)
        """,
        (new_id, name, age, major)
    )

    print("Student added successfully!")

# Save changes
conn.commit()

# Close database
conn.close()

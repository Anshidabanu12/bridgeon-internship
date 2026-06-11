import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks REAL
)
""")

# List of students (name, marks)
students = [
    ("Ravi", 85.5),
    ("Anu", 90.0),
    ("Arjun", 78.5),
    ("Meera", 88.0),
    ("Rahul", 92.5)
]

# Insert students using a loop
for student in students:
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        student
    )

# Save changes
conn.commit()

print("5 students inserted successfully!")

# Display inserted records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

print("\nStudents Table:")
for row in rows:
    print(row)

# Close connection
conn.close()
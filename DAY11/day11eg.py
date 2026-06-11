
import sqlite3

conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    mark REAL,
    grade TEXT
)
''')

# Insert data
cursor.execute(
    'INSERT INTO students (name, mark) VALUES (?, ?)',
    ('john', 89.5)
)

conn.commit()

# Select data
cursor.execute(
    'SELECT * FROM students WHERE mark > ?',
    (76,)
)

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
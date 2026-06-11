import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Create table
def create_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            marks REAL
        )
    """)
    conn.commit()


# Insert data
def insert_student(name, marks):
    cursor.execute(
        "INSERT INTO students (name, marks) VALUES (?, ?)",
        (name, marks)
    )
    conn.commit()
    print("Student added successfully!")


# View all students
def get_all_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if rows:
        print("\nAll Students:")
        for row in rows:
            print(row)
    else:
        print("No students found.")


# Search by ID
def get_student_by_id(student_id):
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    if student:
        print("Student found:")
        print(student)
    else:
        print("Student not found.")


# Update marks
def update_marks(student_id, new_marks):
    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, student_id)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Marks updated successfully!")
    else:
        print("Student not found.")


# Delete student
def delete_student(student_id):
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Students above threshold
def get_students_above(threshold):
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )

    rows = cursor.fetchall()

    if rows:
        print(f"\nStudents with marks above {threshold}:")
        for row in rows:
            print(row)
    else:
        print("No matching students found.")


# Main program
def main():
    create_table()

    while True:
        print("\n====== STUDENT DATABASE SYSTEM ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Students Above Marks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            marks = float(input("Enter marks: "))
            insert_student(name, marks)

        elif choice == "2":
            get_all_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            get_student_by_id(student_id)

        elif choice == "4":
            student_id = int(input("Enter Student ID: "))
            new_marks = float(input("Enter new marks: "))
            update_marks(student_id, new_marks)

        elif choice == "5":
            student_id = int(input("Enter Student ID: "))
            delete_student(student_id)

        elif choice == "6":
            threshold = float(input("Enter threshold marks: "))
            get_students_above(threshold)

        elif choice == "7":
            print("Exiting program...")
            conn.close()
            break

        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    main()
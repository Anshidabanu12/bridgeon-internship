import sqlite3

#DATABSE CONNECTION

conn = sqlite3.connect(
    "task_manager.db",
    check_same_thread=False
)

cursor = conn.cursor()


#USERS TABLE

cursor.execute("""CREATE TABLES IF NOT EXISTS users(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE NOT NULL,
               email TEXT UNIQUE NOT NULL,
               password TEXT NOT NULL
               )
""")


#TASKS TABLE

cursor.execute(""""CREATE TABLE IF NOT EXISTS tasks(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT NOT NULL,
               title TEXT NOT NULL,
               description TEXT,
               priority TEXT,
               due_date TEXT,
               completed INTEGER DEFAULT 0
               )
               """)

conn.commit()

#USER FUCTIONS

def register_users(username, email, password):
    try:
        cursor.execute("""
        INSERT INTO users
                       (username, email, password)
                       VALUES(?, ?, ?)
                       """,
                       (username, email, password)
                       )
        conn.commit()
        return True
    except:
        return False

def login_user(username, password):
    cursor.execute(
        """
        SELECT * FROM users
        WHERE username=? AND password=?
        """,
        (username, password)
    )
    return cursor.fetchall()

#TASK FUCTIONS

def add_task(
        username,
        title,
        description,
        priority,
        due_date
):
    cursor.execute(
        """
        INSERT INTO tasks
        (username, title, description,
        priority, due_date)
        VALUES(?, ?, ?, ?, ?)
        """,
        (
            username,
            title,
            description,
            priority,
            due_date
        )
    )
    conn.commit()

def get_tasks(username):
    cursor.execute(
        """
        SELECT * FROM tasks
        WHERE username=?
      """,
      (username,)
    )
    return cursor.fetchall()

def complete_task(task_id):
    cursor.execute(
        """
        UPDATE tasks
        SET completed=1
        WHERE id=?
         """,
         (task_id)
    )
    conn.commit()

def delete_task(task_id):
    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id=?
        """,
        (task_id,)
    )
    conn.commit()
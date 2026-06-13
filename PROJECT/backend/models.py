# import sqlite3

# #CONNECTION

# conn = sqlite3.connect("task_manager.db", check_same_thread=False)
# cursor = conn.cursor()

# #CREATE TABLE

# def create_table():
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    username TEXT UNIQUE NOT NULL,
#                    email TEXT UNIQUE NOT NULL,
#                    password TEXT NOT NULL
#                    )
#           """)
#     cursor.execute(""" 
#           cursor TABLE IF NOT EXISTES tasks(
#                    id INTEGER PRIMARY KEY AUTOINCREMENT,
#                    username TEXT NOT NULL,
#                    title TEXT NOT NULL,
#                    description TEXT,
#                    priority TEXT,
#                    due_date TEXT,
#                    completed INTEGER DEFAULT 0 
#                    )
#             """)
#     conn.commit()


from pydantic import BaseModel
from datetime import date


class User(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Task(BaseModel):
    title: str
    description: str
    priority: str
    due_date: date
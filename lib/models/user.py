# lib/models/user.py

import sqlite3

class User:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def find_by_id(user_id):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = c.fetchone()
        conn.close()
        return user

    @staticmethod
    def get_all():
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        users = c.fetchall()
        conn.close()
        return users

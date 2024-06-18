# lib/models/grocery.py

import sqlite3

class Grocery:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("INSERT INTO groceries (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_id(grocery_id):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("SELECT * FROM groceries WHERE id=?", (grocery_id,))
        grocery = c.fetchone()
        conn.close()
        return grocery

    @staticmethod
    def get_all():
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("SELECT * FROM groceries")
        groceries = c.fetchall()
        conn.close()
        return groceries

    @staticmethod
    def delete(grocery_id):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("DELETE FROM groceries WHERE id=?", (grocery_id,))
        conn.commit()
        conn.close()

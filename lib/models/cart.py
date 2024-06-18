# lib/models/cart.py

import sqlite3

class CartItem:
    def __init__(self, user_id, grocery_id, quantity):
        self.user_id = user_id
        self.grocery_id = grocery_id
        self.quantity = quantity

    def save(self):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("INSERT INTO cart (user_id, grocery_id, quantity) VALUES (?, ?, ?)",
                  (self.user_id, self.grocery_id, self.quantity))
        conn.commit()
        conn.close()

    @staticmethod
    def get_items_by_user_id(user_id):
        conn = sqlite3.connect('store.db')
        c = conn.cursor()
        c.execute("SELECT * FROM cart WHERE user_id=?", (user_id,))
        items = c.fetchall()
        conn.close()
        return items

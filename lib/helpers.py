# lib/helpers.py

from models.user import User
from models.grocery import Grocery
from models.cart import CartItem
from utils import validate_integer_input

def exit_program():
    print("Goodbye!")
    exit()

def add_user(c, conn):
    name = input("Enter user's name: ")
    user = User(name)
    user.save()
    print(f"User '{name}' added successfully.")
    view_groceries(c, conn)

def find_user_by_id(c, conn, user_id):
    user = User.find_by_id(user_id)
    if user:
        print(f"User found: ID={user[0]}, Name={user[1]}")
    else:
        print(f"No user found with ID={user_id}")

def list_all_users(c, conn):
    users = User.get_all()
    if users:
        print("List of all users:")
        for user in users:
            print(f"ID={user[0]}, Name={user[1]}")
    else:
        print("No users found.")

def add_groceries(c, conn):
    name = input("Enter grocery name: ")
    grocery = Grocery(name)
    grocery.save()
    print(f"Grocery '{name}' added successfully.")

def delete_groceries(c, conn):
    grocery_id = validate_integer_input("Enter grocery ID to delete: ")
    Grocery.delete(grocery_id)
    print(f"Grocery ID '{grocery_id}' deleted successfully.")

def view_cart(c, conn, user_id):
    cart_items = CartItem.get_items_by_user_id(user_id)
    if cart_items:
        print(f"Items in your cart (User ID: {user_id}):")
        for item in cart_items:
            grocery = Grocery.get_by_id(item[2])  # Assuming index 2 is 'grocery_id'
            print(f"{grocery[1]} - Quantity: {item[3]}")
    else:
        print("Your cart is empty.")

def update_cart(c, conn, user_id):
    # Implement logic to update user's cart
    pass

def view_groceries(c, conn):
    groceries_data = Grocery.get_all()
    print("Available groceries:")
    for grocery in groceries_data:
        print(f"{grocery[0]}. {grocery[1]}")

    user_id = validate_integer_input("Enter your user ID: ")
    grocery_id = validate_integer_input("Enter the ID of the grocery you want to add to your cart: ")
    quantity = validate_integer_input("Enter quantity: ")

    cart_item = CartItem(user_id, grocery_id, quantity)
    cart_item.save()

    print(f"Added {quantity} of grocery ID {grocery_id} to your cart.")

# lib/cli.py

import sqlite3
from helpers import (
    exit_program,
    add_user,
    find_user_by_id,
    list_all_users,
    add_groceries,
    delete_groceries,
    view_cart,
    update_cart,
    view_groceries
)

conn = sqlite3.connect('store.db')
c = conn.cursor()

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "1":
            exit_program()
        elif choice == "2":
            add_user(c, conn)
        elif choice == "3":
            add_groceries(c, conn)
        elif choice == "4":
            delete_groceries(c, conn)
        elif choice == "5":
            user_id = int(input("Enter your user ID: "))
            view_cart(c, conn, user_id)
        elif choice == "6":
            user_id = int(input("Enter your user ID: "))
            update_cart(c, conn, user_id)
        elif choice == "7":
            view_groceries(c, conn)
        elif choice == "8":
            user_id = int(input("Enter user ID to find: "))
            find_user_by_id(c, conn, user_id)
        elif choice == "9":
            list_all_users(c, conn)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("1. Exit the program")
    print("2. Add a user")
    print("3. Add new groceries (only manager)")
    print("4. Delete groceries (only manager)")
    print("5. View cart")
    print("6. Update cart")
    print("7. View groceries")
    print("8. Find user by ID")
   
if __name__ == "__main__":
    main()

conn.close()

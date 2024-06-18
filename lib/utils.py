# lib/utils.py

def validate_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def confirm_action(prompt):
    while True:
        response = input(prompt + " (yes/no): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def generate_unique_id():
    import uuid
    return uuid.uuid4().hex

"""
File: password_checker.py
Description: Checks the length of a password.
Author: Shree Tharani
"""

def get_password_length(password: str) -> int:
    return len(password)

def main():
    password = input("Enter password: ").strip()
    print("Password length:", get_password_length(password))

if __name__ == "__main__":
    main()

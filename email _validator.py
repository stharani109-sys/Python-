"""
File: email_validator.py
Description: Validates an email address.
Author: Shree Tharani
"""

def is_valid_email(email: str) -> bool:
    """
    Check if the email contains basic valid characters.

    Args:
        email (str): Email address entered by user

    Returns:
        bool: True if valid, False otherwise
    """
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True


def main():
    """Main function to run the email validator."""
    email = input("Enter email address: ").strip()
    if is_valid_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")


if __name__ == "__main__":
    main()

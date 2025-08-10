import re


def check_password_strength(password):
    # Criteria checks
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character (!@#$%^&* etc.)."

    return True, "Password is strong."


# Main script
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    is_strong, message = check_password_strength(user_password)
    print(message)

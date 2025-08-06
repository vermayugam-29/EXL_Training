def validate_user_id_password(user_id, password):
    if len(password) < 8:
        return False
    if len(user_id) < 5:
        return False
    if not any (char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any (char in "!@#$%^&*()_+-=" for char in password):
        return False
    return True
def is_strong_password(password):
    if len(password) < 8:
        return False

    if not any(char.isupper() for char in password):
        return False

    if sum(char.isdigit() for char in password) < 3:
        return False

    return True

while True:
    user_password = input("Придумайте пароль: ")
    
    if is_strong_password(user_password):
        print("Это надёжный пароль.")
        break
    else:
        print("Пароль ненадёжный. Попробуйте ещё раз.")

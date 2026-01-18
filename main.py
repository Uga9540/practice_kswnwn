def main():
    """
    Основная функция программы.
    """
    print("--- Git Practice Project ---")
    print("Status: practice is done")

    user_name = input("Введите ваше имя для приветствия: ")

    if user_name:
        greet_user(user_name)
    else:
        greet_user("Anonymous")


def greet_user(name):
    """
    Функция приветствия пользователя.
    """
    message = f"Hello, {name}! Welcome to your first Git repository."
    print(message)
    return message


if __name__ == "__main__":
    main()
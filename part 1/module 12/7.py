import random

def rock_paper_scissors():
    user_choice = input("Выберите камень, ножницы или бумагу: ").lower()
    computer_choice = random.choice(["камень", "ножницы", "бумага"])

    print("")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы победили!")
    else:
        print("Компьютер победил!")
    
    print("")

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("")
    print("Угадайте число от 1 до 100.")

    while True:
        user_guess = input("Введите вашу догадку: ")
        attempts += 1

        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Введите корректное число.")
            continue

        if user_guess == secret_number:
            print(f"\nПоздравляю! Вы угадали число {secret_number} за {attempts} попыток.\n")
            break
        elif user_guess < secret_number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")

def mainMenu():
    while True:
        print("Главное меню:")
        print("1. Игра 'Камень, ножницы, бумага'")
        print("2. Игра 'Угадай число'")
        print("3. Выход")

        choice = input(">> ")

        if choice == "1":
            rock_paper_scissors()
        elif choice == "2":
            guess_the_number()
        elif choice == "3":
            print("\nСпасибо за игру!\n")
            break
        else:
            print("\nНекорректный выбор. Пожалуйста, выберите опцию из меню.\n")

mainMenu()

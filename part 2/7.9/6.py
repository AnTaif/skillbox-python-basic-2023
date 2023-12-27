contacts = {}

while True:
    print("Введите номер действия:")
    print("1. Добавить контакт")
    print("2. Найти человека")

    choice = input()

    if choice == "1":
        print("Введите имя и фамилию нового контакта (через пробел):")
        name, surname = input().split()
        key = (name, surname)

        if key in contacts:
            print("Такой человек уже есть в контактах.")
        else:
            print("Введите номер телефона:")
            phone = input()
            contacts[key] = phone
            print("Текущий словарь контактов:", contacts)
    elif choice == "2":
        print("Введите фамилию для поиска:")
        search_surname = input().lower()

        found_contacts = [(name, surname, phone) for (name, surname), phone in contacts.items() if surname.lower() == search_surname]

        if found_contacts:
            print("Результаты поиска:")
            for name, surname, phone in found_contacts:
                print(f"{name} {surname} {phone}")
        else:
            print("Контакты с такой фамилией не найдены.")
    else:
        print("Некорректный выбор. Пожалуйста, введите 1 или 2.")

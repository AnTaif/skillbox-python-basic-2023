guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")

    action = input("Гость пришёл или ушёл? ").lower()

    if action == 'пора спать':
        print("Вечеринка закончилась, все легли спать.")
        break

    if action == 'пришёл' or action == 'пришел':
        if len(guests) < 6:
            new_guest = input("Имя гостя: ")
            guests.append(new_guest)
            print(f"Привет, {new_guest}!")
        else:
            print("Прости, но мест нет.")
    elif action == 'ушёл' or action == 'ушел':
        if len(guests) > 0:
            left_guest = input("Имя гостя: ")
            if left_guest in guests:
                guests.remove(left_guest)
                print(f"Пока, {left_guest}!")
            else:
                print(f"{left_guest} не был на вечеринке.")
        else:
            print("Некого прощать, никто не пришел.")
    else:
        print("Некорректный ввод. Пожалуйста, введите 'пришёл', 'ушёл' или 'пора спать'.")
input("Загадайте число от 1 до 100 (включительно). \nНажмите Enter, когда будете готовы.")

low = 1
high = 100
tries = 0

while low <= high:
    mid = (low + high) // 2
    answer = int(input(f"Твоё число равно, меньше или больше, чем {mid}? (1 - равно, 2 - больше, 3 - меньше): "))

    if answer == 1:
        print(f"Компьютер угадал ваше число {mid} за {tries + 1} попыток.")
        break
    elif answer == 2:
        low = mid + 1
    elif answer == 3:
        high = mid - 1
    
    tries += 1

if low > high:
    print("Вы допустили ошибку при ответах.")

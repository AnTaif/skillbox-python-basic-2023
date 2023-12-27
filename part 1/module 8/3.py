reverse_timer = int(input("Введите время (в секундах) до обнуления таймера: "))

for time_left in range(reverse_timer-1, -1, -1):
    print(f"Осталось {time_left} секунд")

    user_response = input("Готовы ли вы забрать еду? ('0' - Нет, '1' - Да): ")

    if user_response == '1':
        break

if (time_left == 0):
    print("Ваша еда готова, осторожно горячо!")
else:
    print(f"Ваша еда готова, можете забрать! Прервано на {reverse_timer - time_left} секунде.")

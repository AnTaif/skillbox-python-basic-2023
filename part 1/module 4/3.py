today = int(input("Введите сегодняшнее число: "))

is_even = today % 2 == 0

if (is_even):
    print("Пора за работу!")
else:
    print("Сегодня можно отдохнуть.")

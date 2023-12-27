def sum_of_digits(number):
    return sum(map(int, str(number)))

def max_digit(number):
    return max(map(int, str(number)))

def min_digit(number):
    return min(map(int, str(number)))

while True:
    try:
        number = int(input("Введите число: "))
        action = input("Выберите действие (сумма/максимум/минимум): ")

        match action:
            case "сумма":
                result = sum_of_digits(number)
            case "максимум":
                result = max_digit(number)
            case "минимум":
                result = min_digit(number)
            case _:
                print("Некорректное действие")
                continue

        print(f"Результат: {result}")

    except ValueError:
        print("Введите корректное число")

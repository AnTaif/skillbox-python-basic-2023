def reverse_number(number):
    reversed_number = str(number)[::-1]
    return reversed_number

while True:
    try:
        num = int(input("Введите число: "))
        if num == 0:
            break

        reversed_num = reverse_number(num)
        print(f"Число наоборот: {reversed_num}")

    except ValueError:
        print("Введите корректное число")

print("Программа завершена!")

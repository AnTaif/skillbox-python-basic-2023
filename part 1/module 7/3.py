num = int(input("Введите число: "))
factorial = 1

for i in range(2, num + 1):
    factorial *= i

print(f"Факториал числа {num} равен {factorial}")

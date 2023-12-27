count = 0

for i in range(1, 11):
    number = int(input(f"Введите {i} число: "))
    if number > 0 and number % 2 == 0:
        count += 1

print("Количество положительных четных чисел:", count)

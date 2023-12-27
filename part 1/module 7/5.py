a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

total_sum = 0
count = 0

for number in range(a, b + 1):
    if number % 3 == 0:
        total_sum += number
        count += 1

if count > 0:
    average = total_sum / count
    print(f"Среднее арифметическое кратных 3 чисел в интервале [{a}; {b}]: {average}")
else:
    print("В указанном интервале нет чисел, кратных 3")

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

sum_of_numbers = 0
count = 0

for num in range(a, b + 1):
    if num % c == 0:
        sum_of_numbers += num
        count += 1

if count > 0:
    average = sum_of_numbers / count
    print(f"Среднее арифметическое чисел от {a} до {b}, кратных {c}, равно {average}")
else:
    print(f"В указанном диапазоне нет чисел, кратных {c}")

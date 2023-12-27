num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

diff = abs(num1 - num2)

max_num = int((num1 + num2 + diff) / 2)

print("Наибольшее число:", max_num)

X = float(input("Введите начальную сумму вклада: "))
Y = float(input("Введите желаемую сумму: "))
P = float(input("Введите годовой процент: "))

years = 0

while X < Y:
    X += X * (P / 100)
    X = int(X)
    years += 1

print(f"Через {years} лет вклад составит не менее {Y}, рублей.")

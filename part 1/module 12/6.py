def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = gcd(num1, num2)
print(f"Наибольший общий делитель: {result}")

def calculate(n):
    return (-1)**n * (1 / 2**n)

n = int(input("Введите N: "))
total = 0.0

for i in range(n):
    total += calculate(i)

print("Ответ:", total)

import math

n = int(input("Введите кол-во чисел: "))

for i in range(n):
    x = float(input("Введите число: "))
    if x > 0:
        x = math.ceil(x)
        result = math.log(x)
        print(f'x = {x} \t log(x) = {result}')
    elif x < 0:
        x = math.floor(x)
        result = math.exp(x)
        print(f'x = {x} \t exp(x) = {result}')
    else:
        print(f'x = {x}')

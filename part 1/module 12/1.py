def summa_n(n):
    sum_n = 0
    for i in range(n):
        sum_n += i + 1
    
    return sum_n

n = int(input("Введите число: "))

sum_n = summa_n(n)

print(f"Я знаю, что сумма чисел от 1 до {n} равна {sum_n}")

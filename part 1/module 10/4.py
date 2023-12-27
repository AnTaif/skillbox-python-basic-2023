def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

count = int(input("Введите количество чисел: "))
prime_count = 0

for i in range(count):
    n = int(input("Введите число: "))

    if is_prime(n):
        prime_count += 1
    
print("Количество простых чисел в последовательности:", prime_count)

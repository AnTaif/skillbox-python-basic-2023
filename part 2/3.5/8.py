def make_symmetric(sequence):
    n = len(sequence)
    additions = []
    
    for i in range(n // 2):
        if sequence[i] != sequence[n - 1 - i]:
            additions.append(sequence[n - 1 - i])
    
    return len(additions), additions[::-1]

n = int(input("Количество чисел: "))

sequence = []
for i in range(n):
    num = int(input("Число: "))
    sequence.append(num)

min_additions, numbers_to_add = make_symmetric(sequence)

print(f"Нужно приписать чисел: {min_additions}")
print(f"Сами числа: {numbers_to_add}")
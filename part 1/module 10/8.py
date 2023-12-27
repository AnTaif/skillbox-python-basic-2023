depth = int(input("Введите глубину ямы: "))

print('')

for i in range(1, depth + 1):
    numbers_row = ''
    empty_space = '.' * (depth * 2 - i * 2)

    for j in range(i):
        numbers_row += str(depth - j)

    row = numbers_row + empty_space + numbers_row[::-1]

    print(row)

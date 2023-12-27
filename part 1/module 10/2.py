rows = int(input("Введите число: "))

for row in range(1, rows + 1):
    for n in range(row):
        print(row, end='  ')
    
    print('')

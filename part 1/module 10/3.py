width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))

vertical_symbol = '|'

for row in range(height):
    if (row == 0 or row == height - 1):
        horizontal_symbol = '-'
    else:
        horizontal_symbol = ' '
    
    print(vertical_symbol, end='')
    for column in range(1, width - 1):
        print(horizontal_symbol, end='')
    print(vertical_symbol)

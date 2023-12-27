levels = int(input("Введите количество уровней пирамиды: "))

current_number = 1
for level in range(1, levels + 1):
    row = "   " * (levels - level) 
    
    for column in range(level):
        row += str(current_number)
        current_number += 2
        row += "    "

    print(row)

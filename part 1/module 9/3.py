rows = int(input("Введите кол-во рядов: "))
row_seats = int(input("Введите кол-во сидений в ряду: "))
meters_between = int(input("Введите кол-во метров между рядами: "))

print("\nСцена\n")

for row in range(rows):
    row_scheme = '=' * row_seats + '*' * meters_between + '=' * row_seats
    print(row_scheme)

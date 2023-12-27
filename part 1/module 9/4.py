x_max = 15
y_max = 20

x = 8
y = 10

while True:
    command = input(f"Марсоход находится на позиции {x}, {y}, введите команду (WASD): ")

    match command.upper():
        case 'W':
            if (y < y_max):
                y += 1
        case 'A':
            if (0 < x):
                x -= 1
        case 'S':
            if (0 < y):
                y -= 1
        case 'D':
            if (x < x_max):
                x += 1

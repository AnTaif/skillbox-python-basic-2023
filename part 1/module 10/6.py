height = int(input("Введите высоту пирамидки: "))

for row in range(1, height + 1):
    spaces = " " * (height - row)
    hashtags = "#" * (2 * row - 1)

    print(spaces + hashtags)

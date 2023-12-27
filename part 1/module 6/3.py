num = int(input("Введите число: "))

count = 0

if (num == 0):
    count = 1
else:
    while (num != 0):
        count += 1
        num //= 10

print("Количество цифр в числе:", count)

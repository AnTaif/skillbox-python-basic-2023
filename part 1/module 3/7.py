num = int(input("Введите четырехзначное число: "))

thousands_digit = num // 1000
hundreds_digit = (num // 100) % 10
tens_digit = (num // 10) % 10
ones_digit = num % 10

digits = [thousands_digit, hundreds_digit, tens_digit, ones_digit]

for digit in digits:
    print(digit, end='  ')
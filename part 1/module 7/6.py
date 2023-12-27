for number in range(10, 100):
    tens_digit = number // 10
    ones_digit = number % 10

    if number == 3 * tens_digit * ones_digit:
        print(number)

def count_numbers(num):
    num_count = 0
    temp = num

    while temp > 0:
        num_count += 1
        temp = temp // 10

def change_number(num):
    last_digit = num % 10
    first_digit = num // 10 ** (num_count - 1)
    between_digits = num % 10 ** (num_count - 1) // 10
    return last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit

def main():
    first_n = int(input("Введите первое число: "))

    first_num_count = count_numbers(first_n)

    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
    else:
        first_n = change_number(first_n)
        print('Изменённое первое число:', first_n)

    second_n = int(input("\nВведите второе число: "))

    second_num_count = count_numbers(second_n) 

    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        second_n = change_number(second_n)
        print('Изменённое второе число:', second_n)

    print('\nСумма чисел:', first_n + second_n)

main()

def check_phone_numbers(phone_numbers):
    for number in phone_numbers:
        if len(number) == 10:
            if number[0] in ['8', '9']:
                if number[1:].isdigit():
                    print(f'{number}: всё в порядке')
                else:
                    print(f'{number}: не подходит (остальные символы не являются цифрами)')
            else:
                print(f'{number}: не подходит (номер не начинается с 8 или 9)')
        else:
            print(f'{number}: не подходит (неверная длина)')

phone_numbers = ['9999999999', '999999-999', '99999x9999']
check_phone_numbers(phone_numbers)

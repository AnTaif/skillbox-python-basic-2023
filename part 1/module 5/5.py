user_input = input("Введите три числа через пробел: ")

numbers = list(map(int, user_input.split()))

unique_numbers = set(numbers)

if len(unique_numbers) == 1:
    print(3)
elif len(unique_numbers) == 2:
    print(2)
else:
    print(0)

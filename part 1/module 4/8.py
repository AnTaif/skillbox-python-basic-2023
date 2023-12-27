user_input = input("Введите три числа через пробел: ")

numbers = list(map(int, user_input.split()))

max_number = max(numbers)

print(max_number)

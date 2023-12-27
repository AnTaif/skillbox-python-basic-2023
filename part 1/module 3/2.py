user_input = input("Введите 4 числа через пробел: ")

numbers = list(map(int, user_input.split()))

first_sum = numbers[0] + numbers[1]
second_sum = numbers[2] + numbers[3]

result = first_sum / second_sum

print(result)

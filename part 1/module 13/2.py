def maximum_of_two(a, b):
    if (a >= b):
        return a
    else:
        return b
    
def maximum_of_three(a, b, c):
    return maximum_of_two(a, maximum_of_two(b, c))

user_input = input("Введите три числа через пробел: ")
numbers = list(map(float, user_input.split()))

result = maximum_of_three(numbers[0], numbers[1], numbers[2])
print("Максимум из трех чисел:", result)

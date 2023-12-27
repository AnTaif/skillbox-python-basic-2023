def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

num1_reversed = reverse_number(num1)
num2_reversed = reverse_number(num2)

print("")
print("Первое число наоборот:", num1_reversed)
print("Второе число наоборот:", num2_reversed)

num_sum = num1_reversed + num2_reversed

print("")
print("Сумма:", num_sum)
print("Сумма наоборот:", num1 + num2)

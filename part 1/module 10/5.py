def sum_of_digits(number):
    return sum(map(int, str(number)))

n = int(input("Введите количество чисел: "))

max_sum = 0
max_sum_number = 0

for i in range(n):
    num = int(input(f"Введите {i+1}-е число: "))
    current_sum = sum_of_digits(num)
    
    if current_sum > max_sum:
        max_sum = current_sum
        max_sum_number = num

print(f"Число с наибольшей суммой цифр: {max_sum_number}")
print(f"Сумма его цифр: {max_sum}")

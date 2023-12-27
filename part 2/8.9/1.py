def print_numbers_recursive(num):
    if num > 0:
        print_numbers_recursive(num - 1)
        print(num)

n = int(input("Введите n: "))

print_numbers_recursive(n)

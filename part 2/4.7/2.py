N = int(input("Введите длину списка: "))

result_list = [1 if i % 2 == 0 else i % 5 for i in range(N)]

print(f"\nРезультат: {result_list}")

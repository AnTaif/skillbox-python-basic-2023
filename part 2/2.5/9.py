import random
import time

start_creating_list = time.perf_counter()
def creating_list(quantity):
    rand_list = []

    for _ in range(quantity):
        number = random.randint(-100, 100)
        float_num = random.uniform(-100, 100)
        float_num = round(float_num, 2)
        digit = random.randint(0, 9)
        rand_list.append(digit)
        rand_list.append(float_num)
        rand_list.append(number)

    return rand_list

creating_list_speed = time.perf_counter() - start_creating_list
print(f"Скорость генерации списка: {creating_list_speed}\n")

numbers_list = creating_list(10)

print(f"Список:\n{numbers_list}")
print(f"Длина списка: {len(numbers_list)}")
l = len(numbers_list)
for i in range(l):
    if numbers_list[i] > 0 and numbers_list[i] % 2 == 0:
        print(f"{numbers_list[i]}", end = '    ')
list_a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

list_a.extend(b)

print(f"Количество цифр 5 при первом объединении: {list_a.count(5)}")

while 5 in list_a:
    list_a.remove(5)

print(f"Cписок: {list_a}")

list_a.extend(c)

print(f"Количество цифр 3 при втором объединении: {list_a.count(3)}")
print(f"Итоговый список: {list_a}")
user_input = input("Введите оценки учеников через пробел: ")

marks = list(map(int, user_input.split()))

excellent_count = 0
good_count = 0
average_count = 0

for mark in marks:
    if mark == 5:
        excellent_count += 1
    elif mark == 4:
        good_count += 1
    elif mark == 3:
        average_count += 1

if excellent_count > good_count and excellent_count > average_count:
    print("Сегодня больше отличников")
elif good_count > excellent_count and good_count > average_count:
    print("Сегодня больше хорошистов")
else:
    print("Сегодня больше троечников")

def last_person_standing(n, k):
    circle = list(range(1, n + 1))
    index = 0

    while len(circle) > 1:
        index = (index + k - 1) % len(circle)
        removed_person = circle.pop(index)
        print(f"Выбывает человек под номером {removed_person}")
        print(f"Текущий круг людей: {circle}")
    
    return circle[0]

num_people = int(input("Количество человек: "))
k_value = int(input("Какое число в считалке? "))

last_person = last_person_standing(num_people, k_value)

print(f"\nОстался человек под номером {last_person}")
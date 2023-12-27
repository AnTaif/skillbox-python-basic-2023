print("Задача 1:")

common_elements = [x for x in array_1 if x in array_2 and x in array_3]
print("Решение без множеств:", common_elements)

set_1 = set(array_1)
set_2 = set(array_2)
set_3 = set(array_3)
common_elements_set = list(set_1.intersection(set_2, set_3))

print("Решение с множествами:", common_elements_set)

print("\nЗадача 2:")

unique_elements = [x for x in array_1 if x not in array_2 and x not in array_3]
print("Решение без множеств:", unique_elements)

unique_elements_set = list(set_1.difference(set_2, set_3))
print("Решение с множествами:", unique_elements_set)

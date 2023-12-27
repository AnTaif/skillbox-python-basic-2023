n = int(input('Сколько ящиков будем добавлять?: '))

weight_list = []

for i in range(n):
    weight = int(input(f"Сколько весит {i+1}-й ящик?: "))
    weight_list.append(weight)

weight_list.sort()
print(f"Ящики упорядочены: {weight_list}")

new_weight = int(input('Сколько весит новый ящик?: '))

id = 0

for i, elem in enumerate(weight_list):
    if new_weight < elem:
        id = i
        break
    elif new_weight == elem:
        id += 1
    else:
        if new_weight > weight_list[-1]:
            id = len(weight_list)

weight_list.insert(id, new_weight)    # добавляю новый ящик в место его веса

print(f"Номер, который получит новый ящик: {id}\nНовый список: {weight_list}")
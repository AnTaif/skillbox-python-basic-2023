def var_1():
    i = 0
    id = i + step

    for elem in start_list:
        if id < len(start_list):
            end_list.insert(id, elem)
            id += 1
        elif id == len(start_list):
            id = 0
            end_list.insert(id, elem)
            id += 1
        else:
            print('Ошибка ввода: шаг превышает длину списка.')
            break
        i += 1

def var_2():
    srez_l = start_list[:step]
    srez_r = start_list[step:]
    end_list[1:step] = srez_r + srez_l

start_list = [1, 4, -3, 0, 10]
step = 2
end_list = []

var_2()

print(f"Стартовый список {start_list}\n"
      f"Сдвинутый список: {end_list}")
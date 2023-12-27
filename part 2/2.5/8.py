def selection_sort(some_list: float):
    id_min = 0
    for id_min in range(len(some_list)):
        for id_curr in range(id_min, len(some_list)):
            if some_list[id_curr] < some_list[id_min]:
                some_list[id_curr], some_list[id_min] = some_list[id_min], some_list[id_curr]

    return some_list


if __name__ == '__main__':
    some_list = [4, 8, 5, 6, 9, 1, 3, 2, 7]

    result = selection_sort(some_list)

    print(f"\nИсходный список:\n[4, 8, 5, 6, 9, 1, 3, 2, 7]\n"
          f"\nАлгоритм сортировки выбором:\n{result}")
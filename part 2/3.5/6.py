def find_max_people(rollerblades, foot_sizes):
    rollerblades.sort(reverse=True)
    foot_sizes.sort(reverse=True)

    max_people = 0
    i, j = 0, 0

    while i < len(rollerblades) and j < len(foot_sizes):
        if rollerblades[i] <= foot_sizes[j]:
            max_people += 1
            i += 1
            j += 1
        else:
            j += 1

    return max_people

num_rollerblades = int(input("Количество роликов: "))
rollerblade_sizes = [int(input(f"Размер пары {i + 1}: ")) for i in range(num_rollerblades)]

num_people = int(input("\nКоличество людей: "))
foot_sizes = [int(input(f"Размер ноги человека {i + 1}: ")) for i in range(num_people)]

max_people = find_max_people(rollerblade_sizes, foot_sizes)

print(f"\nНаибольшее количество людей, которые могут взять ролики: {max_people}")
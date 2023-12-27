def find_key_in_dict(dictionary, key, max_depth=None, current_depth=0):
    if isinstance(dictionary, dict):
        if key in dictionary:
            return dictionary[key]
        elif max_depth is None or current_depth < max_depth:
            for value in dictionary.values():
                result = find_key_in_dict(value, key, max_depth, current_depth + 1)
                if result is not None:
                    return result
    return None

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search_key = input("Введите искомый ключ: ")

max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ").lower()
max_depth = None

if max_depth_input == 'y':
    max_depth = int(input("Введите максимальную глубину: "))

result = find_key_in_dict(site, search_key, max_depth)
print("Значение ключа:", result)

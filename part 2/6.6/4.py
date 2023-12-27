def invert_frequency_dict(text):
    frequency_dict = {}

    for char in text:
        if char.isalpha():
            char = char.upper()
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    original_frequency_dict = {}
    for char, count in frequency_dict.items():
        original_frequency_dict.setdefault(count, []).append(char)

    return original_frequency_dict

text = input("Введите текст: ")

result = invert_frequency_dict(text)

print("\nОригинальный словарь частот:")
for char, count in sorted(result.items()):
    print(f"{char} : {count}")

print("\nИнвертированный словарь частот:")
for count, chars in sorted(result.items()):
    print(f"{count} : {chars}")

def find_longest_word(input_string):
    words = input_string.split()
    
    if not words:
        return None, 0

    longest_word = max(words, key=len)
    length = len(longest_word)

    return longest_word, length

user_input = input("Введите строку: ")

longest_word, length = find_longest_word(user_input)

if longest_word:
    print(f"Самое длинное слово: «{longest_word}».")
    print(f"Длина этого слова: {length} символов.")
else:
    print("Строка не содержит слов.")

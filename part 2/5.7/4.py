def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = ' '.join(capitalized_words)
    return result

user_input = input("Введите строку: ")

result = capitalize_first_letter(user_input)
print("Результат:", result)

text = input("Введите текст: ")

words = text.split()
longest_word = ''

for word in words:
    if (len(word) > len(longest_word)):
        longest_word = word

print(f"Самое длинное слово - \"{longest_word}\", {len(longest_word)} букв")

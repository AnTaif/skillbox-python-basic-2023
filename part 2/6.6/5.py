def create_synonym_dict():
    n = int(input("Введите количество пар слов: "))
    synonym_dict = {}

    for _ in range(n):
        pair = input("Введите пару слов через дефис: ").split(' — ')
        word1, word2 = pair[0].lower(), pair[1].lower()
        synonym_dict[word1] = word2
        synonym_dict[word2] = word1

    return synonym_dict

def find_synonym(synonym_dict, word):
    word_lower = word.lower()
    if word_lower in synonym_dict:
        return synonym_dict[word_lower]
    else:
        return None

synonym_dict = create_synonym_dict()

while True:
    user_word = input("Введите слово: ").lower()
    synonym = find_synonym(synonym_dict, user_word)
    
    if synonym:
        print(f"Синоним: {synonym.capitalize()}")
        break
    else:
        print("Такого слова в словаре нет. Попробуйте ещё раз.")

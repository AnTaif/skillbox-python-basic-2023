VOWELS = 'аеёиоуыэюя'

def extract_vowels(text):
    vowels_list = [char.lower() for char in text if char.lower() in VOWELS]
    return vowels_list

user_text = input("Введите текст: ")

vowels_result = extract_vowels(user_text)
vowels_count = len(vowels_result)

print(f"\nСписок гласных букв: {vowels_result}")
print(f"Длина списка: {vowels_count}")

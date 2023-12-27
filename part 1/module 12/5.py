def count_digit(text, digit):
    digit_count = text.count(digit)
    return digit_count

def count_letter(text, letter):
    letter_count = text.lower().count(letter.lower())
    return letter_count

text = input("Введите текст: ")
digit = input("Какую цифру ищем? ")
letter = input("Какую букву ищем? ")

digit_count = count_digit(text, digit)
letter_count = count_letter(text, letter)

print(f"Количество цифр {digit}: {digit_count}")
print(f"Количество букв {letter}: {letter_count}")

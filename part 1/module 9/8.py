word = input("Введите строку: ")

reversed_word = ''

for letter in word:
    reversed_word = letter + reversed_word 

is_palindrome = reversed_word == word

if is_palindrome:
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром!")

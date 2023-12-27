word = input("Введите слово: ")
l = len(word) // 2
count = 0

for i in range(l):
    if word[i] == word[len(word) - 1 - i]:
        count += 1

if count == l:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')
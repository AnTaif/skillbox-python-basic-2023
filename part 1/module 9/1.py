words = []
for i in range(1, 11):
    words.append(input(f"Введите {i} слово: "))

special_word = "Карамба"
member_count = 0

for word in words:
    if word.lower() == special_word.lower():
        member_count += 1

print("Количество человек, которые попали на борт:", member_count)

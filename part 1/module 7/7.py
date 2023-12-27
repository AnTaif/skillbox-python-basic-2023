n = int(input("Введите количество карточек: "))

total_sum = n * (n + 1) // 2

remaining_sum = 0

for i in range(n - 1):
    card_number = int(input("Введите номер оставшейся карточки: "))
    remaining_sum += card_number

lost_card_number = total_sum - remaining_sum

print("Номер пропавшей карточки:", lost_card_number)

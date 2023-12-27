debtors = int(input("Введите количество должников: "))

total_debt = 0


for debtor in range(0, debtors, 5):
    print("Должник с номером", debtor)
    debt = int(input("Сколько должны? "))
    total_debt += debt

print("Общая сумма долга:", total_debt)

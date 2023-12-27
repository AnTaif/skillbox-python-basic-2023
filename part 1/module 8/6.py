educational_grant = float(input("Введите стипендию: "))
expenses = float(input("Введите расходы на проживание: "))

total_needed = 0

for month in range(1, 11):
    if month == 1:
        expenses_for_month = expenses
    else:
        expenses_for_month *= 1.03
    
    total_needed += expenses_for_month - educational_grant

    print(f"месяц траты {expenses_for_month:.2f} не хватает {total_needed:.2f}")

print(f"Нужно попросить у родителей {total_needed:.2f} рублей")

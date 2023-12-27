def calculate_salary(hours):
    return ((200 * hours) / 2**3) + hours


hours = int(input("Введите отработанные часы: "))
credit_balance = int(input("Введите остаток по кредиту: "))
food_cost = int(input("Введите траты на еду: "))

salary = calculate_salary(hours)
money_spending = credit_balance + food_cost

if (salary >= money_spending):
    print("Часов хватает. Можно отдохнуть")
else:
    print("Часов не хватает. Придётся работать больше!")
    
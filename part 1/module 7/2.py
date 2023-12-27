total_salary = 0

for month in range(1, 13):
    salary = float(input(f"Введите зарплату за {month} месяц: "))
    total_salary += salary

average_salary = total_salary / 12
print("Среднегодовая зарплата:", average_salary)

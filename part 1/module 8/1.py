total_groats = 100
monthly_consumption = 4

months = 0

for consume_count in range(4, total_groats, monthly_consumption):
    months += 1
    current_groats = total_groats - consume_count
    print(f"Через {months} мес. у вас должно быть {current_groats} кг гречки в запасе.")

print(f"Гречка закончится через {months + 1} месяцев.")

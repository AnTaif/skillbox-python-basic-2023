working_hours = 8
tasks_completed = 0
phone_calls = 0

print(f"Начался {working_hours} часовой рабочий день.")

current_hour = 1
while (current_hour <= working_hours):
    print(f"{current_hour}-й час")
    
    tasks_completed += int(input("Сколько задач решит Максим? "))
    phone_calls += int(input("Звонит жена. Взять трубку? (1 — да, 0 — нет): "))
    current_hour += 1

print("Рабочий день закончился. Всего выполнено задач:", tasks_completed)

if (phone_calls > 0):
    print("Нужно зайти в магазин.")

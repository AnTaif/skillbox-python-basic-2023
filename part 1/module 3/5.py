user_input = int(input("Введите количество минут: "))

hours = user_input // 60
minutes = user_input % 60

print(f"В {user_input}мин - {hours}ч и {minutes}мин")

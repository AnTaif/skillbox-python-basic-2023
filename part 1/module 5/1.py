experience = int(input("Введите количество опыта: "))

lvl_stages = [1000, 2500, 5000]
lvl = 1

for lvl_stage in lvl_stages:
    if (experience < lvl_stage):
        break
    lvl += 1

print(f"Ваш уровень: {lvl}")

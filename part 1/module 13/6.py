def danger_level(x):
    return x**3 - 3*x**2 - 12*x + 10

max_danger = float(input("Введите максимально допустимый уровень опасности: "))

x = 0.0
step = 1e-3

while danger_level(x) > max_danger:
    x += step

print(f"Приблизительная глубина безопасной кладки: {x:.9f} м")

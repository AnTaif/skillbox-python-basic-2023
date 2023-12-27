import math

def get_volume(raduis):
    return (4/3) * math.pi * radius**3

radius = float(input("Введите радиус случайной планеты: "))

earth_volume = 1.08321e12
planet_volume = get_volume(radius)

if earth_volume > planet_volume:
    ratio = earth_volume / planet_volume
    print(f"Объём планеты Земля больше в {ratio:.3f} раз")
elif earth_volume < planet_volume:
    ratio = planet_volume / earth_volume
    print(f"Объём планеты Земля меньше в {ratio:.3f} раз")
else:
    print("Объем Земли и теоритически возможной планеты равны")

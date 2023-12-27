import re

def find_car_numbers(text):
    private_car_pattern = r'[АВЕКМНОРСТУХ]{1}\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    taxi_pattern = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'

    private_car_numbers = re.findall(private_car_pattern, text)
    taxi_numbers = re.findall(taxi_pattern, text)

    return private_car_numbers, taxi_numbers

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_car_numbers, taxi_numbers = find_car_numbers(text)

print(f"Список номеров частных автомобилей: {private_car_numbers}")
print(f"Список номеров такси: {taxi_numbers}")

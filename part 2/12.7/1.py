class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 1000

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 200

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def calculate_tax(self):
        return self.worth / 500


money = float(input("Введите количество ваших денег: "))
apartment_worth = float(input("Введите стоимость квартиры: "))
car_worth = float(input("Введите стоимость машины: "))
country_house_worth = float(input("Введите стоимость дачи: "))

apartment = Apartment(apartment_worth)
car = Car(car_worth)
country_house = CountryHouse(country_house_worth)

total_tax = apartment.calculate_tax() + car.calculate_tax() + country_house.calculate_tax()
print(f"Общий налог на ваше имущество: {total_tax}")

if money < total_tax:
    print(f"Вам не хватает {total_tax - money} денег.")
else:
    print("У вас достаточно денег для оплаты налога.")

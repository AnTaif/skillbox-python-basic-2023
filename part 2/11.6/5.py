import random

class Person:
    def __init__(self, name, house):
        self.name = name
        self.satiation = 50
        self.house = house

    def eat(self):
        self.satiation += 10
        self.house.food -= 1

    def work(self):
        self.satiation -= 5
        self.house.money += 10

    def play(self):
        self.satiation -= 5

    def go_shopping(self):
        self.house.food += 10
        self.satiation -= 5
        self.house.money -= 10

    def live_one_day(self):
        dice = random.randint(1, 6)

        if self.satiation < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play()

        if self.satiation < 0:
            print(f"{self.name} died of starvation.")
            return False
        else:
            return True

class House:
    def __init__(self):
        self.food = 50
        self.money = 0

house = House()
person1 = Person("Artem", house)
person2 = Person("Alice", house)

for day in range(1, 366):
    print(f"Day {day}:")
    print(f"{person1.name} - Satiation: {person1.satiation}, Food in house: {house.food}, Money: {house.money}")
    print(f"{person2.name} - Satiation: {person2.satiation}, Food in house: {house.food}, Money: {house.money}")

    if not person1.live_one_day() or not person2.live_one_day():
        break

    print("")

print(f"Final State:")
print(f"{person1.name} - Satiation: {person1.satiation}, Food in house: {house.food}, Money: {house.money}")
print(f"{person2.name} - Satiation: {person2.satiation}, Food in house: {house.food}, Money: {house.money}")

import random

class Warrior:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, opponent):
        damage = 20
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name}. {opponent.name}'s health: {opponent.health}")


warrior1 = Warrior("Warrior 1")
warrior2 = Warrior("Warrior 2")

while warrior1.health > 0 and warrior2.health > 0:
    attacker, defender = random.sample([warrior1, warrior2], k=2)
    attacker.attack(defender)

if warrior1.health <= 0:
    print(f"{warrior2.name} wins! {warrior1.name} is defeated.")
else:
    print(f"{warrior1.name} wins! {warrior2.name} is defeated.")

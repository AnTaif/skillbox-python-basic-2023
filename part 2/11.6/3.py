class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def info(self):
        print(f"Parent: {self.name}, Age: {self.age}, Number of Children: {len(self.children)}")

    def comfort_child(self, child):
        print(f"{self.name} comforts {child.name}.")
        child.set_calm()

    def feed_child(self, child):
        print(f"{self.name} feeds {child.name}.")
        child.set_not_hungry()


class Child:
    def __init__(self, name, age, parent):
        self.name = name
        self.age = age
        self.parent = parent
        self.calm = True
        self.hungry = True

    def set_calm(self):
        self.calm = True

    def set_not_calm(self):
        self.calm = False

    def set_not_hungry(self):
        self.hungry = False

    def info(self):
        print(f"Child: {self.name}, Age: {self.age}, Calm: {self.calm}, Hungry: {self.hungry}")


parent = Parent("John", 40)
child1 = Child("Alice", 10, parent)
child2 = Child("Bob", 8, parent)

parent.children.extend([child1, child2])

parent.info()
for child in parent.children:
    child.info()

parent.comfort_child(child1)
parent.feed_child(child2)

for child in parent.children:
    child.info()

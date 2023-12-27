class Substance:
    def __str__(self):
        return self.name

    def __call__(self, x, y):
        return x + y


class Water(Substance):
    name = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()

        elif isinstance(other, Fire):
            return Steam()

        elif isinstance(other, Earth):
            return Mud()

        else:
            return None


class Air(Substance):
    name = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()

        elif isinstance(other, Fire):
            return Lightning()

        elif isinstance(other, Earth):
            return Dust()

        else:
            return None


class Fire(Substance):
    name = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()

        elif isinstance(other, Earth):
            return Lava()

        elif isinstance(other, Water):
            return Steam()

        else:
            return None


class Earth(Substance):
    name = 'Земля'

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()

        elif isinstance(other, Fire):
            return Lava()

        elif isinstance(other, Water):
            return Mud()

        else:
            return None


class Storm(Substance):
    name = 'Шторм'


class Steam(Substance):
    name = 'Пар'


class Mud(Substance):
    name = 'Грязь'


class Lightning(Substance):
    name = 'Молния'


class Dust(Substance):
    name = 'Пыль'


class Lava(Substance):
    name = 'Лава'


water = Water()
air = Air()
fire = Fire()
earth = Earth()

storm = Storm()
steam = Steam()
mud = Mud()
lightning = Lightning()
dust = Dust()
lava = Lava()

print(storm(water, air), steam(water, fire), mud(water, earth), lightning(air, fire), dust(air, earth), lava(fire, earth))

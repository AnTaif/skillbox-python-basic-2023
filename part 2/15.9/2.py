import math

class MyMath:
    @staticmethod
    def circle_len(radius):
        return 2 * math.pi * radius

    @staticmethod
    def circle_sq(radius):
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side_length):
        return side_length ** 3

    @staticmethod
    def sphere_surface_area(radius):
        return 4 * math.pi * radius ** 2

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
res_3 = MyMath.cube_volume(side_length=4)
res_4 = MyMath.sphere_surface_area(radius=3)

print(res_1)
print(res_2)
print(res_3)
print(res_4)

from typing import List

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

cubed_floats = [round(x**3, 3) for x in floats]

selected_names = [name for name in names if len(name) >= 5]

product_of_numbers = 1
for num in numbers:
    product_of_numbers *= num

print("Cubed Floats:", cubed_floats)
print("Selected Names:", selected_names)
print("Product of Numbers:", product_of_numbers)

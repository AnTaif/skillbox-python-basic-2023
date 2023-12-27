print("Введите местоположение коня:")
x_knight = int(float(input("X: ")) * 10)
y_knight = int(float(input("Y: ")) * 10)


print("Введите местоположение точки на доске:")
x_point = int(float(input("X: ")) * 10)
y_point = int(float(input("Y: ")) * 10)

x_distance = abs(x_knight - x_point)
y_distance = abs(y_knight - y_point)

is_valid_move = (x_distance == 2 and y_distance == 1) or (x_distance == 1 and y_distance == 2)

print(f"Конь в клетке ({x_knight}, {y_knight}). Точка в клетке ({x_point}, {y_point}).")

if (is_valid_move):
    print("Да, конь может ходить в эту точку.")
else:
    print("Конь не может ходить в эту точку.")

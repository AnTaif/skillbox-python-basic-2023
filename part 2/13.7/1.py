class SquaresIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration


def generate_squares(n):
    current = 1
    while current <= n:
        yield current ** 2
        current += 1


n_value = int(input("Введите число N: "))

print("\nКласс-итератор")
squares_iter = SquaresIterator(n_value)
for square in squares_iter:
    print(square)

print("\nФункция-генератор")
for square in generate_squares(n_value):
    print(square)

print("\nГенераторное выражение")
squares = (i ** 2 for i in range(1, n_value + 1))
for square in squares:
    print(square)


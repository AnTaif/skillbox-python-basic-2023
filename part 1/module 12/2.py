def test():
    n = int(input("Введите целое число: "))
    if (n > 0):
        positive()
    else:
        negative()

def positive():
    print("Положительное")

def negative():
    print("Отрицательное")

test()

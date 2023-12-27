taken_number = 7
tries = 0

while (True):
    num = int(input("Введите число: "))
    tries += 1

    if (num == taken_number):
        break

    if (num > taken_number):
        print("Число больше, чем нужно. Попробуйте ещё раз!") 
    else :
        print("Число меньше, чем нужно. Попробуйте ещё раз!") 

print("Вы угадали! Число попыток:", tries)

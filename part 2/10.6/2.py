import random
import os

base_path = os.path.dirname(os.path.abspath(__file__))

sum_of_numbers = 0

with open(os.path.join(base_path, "out_file.txt"), "a") as file:
    while sum_of_numbers < 777:
        try:
            user_input = int(input("Введите число: "))
            file.write(str(user_input) + '\n')
            sum_of_numbers += user_input

            if random.randint(1, 13) == 1:
                raise Exception("Вас постигла неудача!")

        except ValueError:
            print("Введите корректное число.")

    print("Вы успешно выполнили условие для выхода из порочного цикла!")

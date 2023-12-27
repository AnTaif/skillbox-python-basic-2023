import random
import os

base_path = os.path.dirname(os.path.abspath(__file__))

class KillError(Exception):
    pass

class DrunkError(Exception):
    pass

class CarCrashError(Exception):
    pass

class GluttonyError(Exception):
    pass

class DepressionError(Exception):
    pass

def one_day():
    karma = random.randint(1, 7)
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    return karma

karma_goal = 500
current_karma = 0

with open(os.path.join(base_path, "karma.log"), "a") as log_file:
    while current_karma < karma_goal:
        try:
            karma_for_day = one_day()
            current_karma += karma_for_day
            print(f"Получено кармы за день: {karma_for_day}. Текущая карма: {current_karma}")
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as e:
            log_file.write(f"Исключение: {type(e).__name__}\n")
            print(f"Произошло исключение: {type(e).__name__}. Запись в лог.")
    print("Достигнута карма для просветления! Поздравляем!")

import time
from datetime import datetime

def log_methods(time_format):
    def decorator(cls):
        class Wrapper:
            def __init__(self, *args, **kwargs):
                self.wrapped = cls(*args, **kwargs)

            def __getattr__(self, name):
                method = getattr(self.wrapped, name)

                if callable(method) and not name.startswith("__"):
                    def wrapped_method(*args, **kwargs):
                        start_time = time.time()
                        formatted_time = datetime.now().strftime(time_format)

                        print(f"Запускается '{cls.__name__}.{name}'. Дата и время запуска: {formatted_time}.")

                        result = method(*args, **kwargs)

                        end_time = time.time()
                        elapsed_time = round(end_time - start_time, 3)
                        print(f"Завершение '{cls.__name__}.{name}', время работы = {elapsed_time} s.")

                        return result

                    return wrapped_method
                else:
                    return method

        return Wrapper

    return decorator

@log_methods("%b %d %Y — %H:%M:%S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1.')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

@log_methods("%b %d %Y — %H:%M:%S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника.")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника.")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

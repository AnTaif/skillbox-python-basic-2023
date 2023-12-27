from typing import Callable

def decorator_with_args_for_any_decorator(decorator_func):
    def wrapper(*args, **kwargs):
        print(f"Переданные арги и кварги в декоратор: {args} {kwargs}")
        return decorator_func(*args, **kwargs)

    return wrapper

@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapper(*func_args, **func_kwargs):
        print(f"Привет, {func_args[0]} {func_args[1]}")
        func(*func_args, **func_kwargs)
    return wrapper

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)

decorated_function("Юзер", 101)

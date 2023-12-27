import time

def delay_execution(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@delay_execution(3)
def example_function():
    print("Function executed after a 3-second delay.")

example_function()

import logging
import traceback
from functools import wraps
from datetime import datetime
import os

base_path = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(filename=os.path.join(base_path, 'function_errors.log'), level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"Function: {func.__name__}")
            print(f"Documentation: {func.__doc__}")
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            error_message = f"Error in function {func.__name__}: {str(e)}"
            logging.error(error_message)
            traceback.print_exc()
    return wrapper

@logging_decorator
def example_function():
    print("Example function.")
    raise ValueError("This is a sample error.")

@logging_decorator
def another_function():
    print("Another function.")
    result = 10 / 0

example_function()
another_function()

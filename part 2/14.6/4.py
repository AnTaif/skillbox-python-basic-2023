def counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Function {func.__name__} has been called {wrapper.calls} times.")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@counter
def example_function():
    print("Executing example function.")

@counter
def another_function():
    print("Executing another function.")

example_function()
example_function()
another_function()

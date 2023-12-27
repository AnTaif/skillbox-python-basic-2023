class App:
    def __init__(self):
        self.routes = {}

    def get(self, path):
        return self.routes.get(path)

    def add_route(self, path, callback_func):
        self.routes[path] = callback_func

def callback(path):
    def decorator(func):
        app.add_route(path, func)

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper
    return decorator

app = App()

@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

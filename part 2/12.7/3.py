class MyDict(dict):
    def get(self, key, default=None):
        return super().get(key, 0)

my_dict = MyDict({'a': 1, 'b': 2, 'c': 3})

result = my_dict.get('d')
print(result)

result = my_dict.get('b')
print(result)

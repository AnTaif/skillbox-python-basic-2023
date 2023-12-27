def custom_zip(iterable1, iterable2):
    iterator1, iterator2 = iter(iterable1), iter(iterable2)
    sentinel = object()

    while True:
        value1 = next(iterator1, sentinel)
        value2 = next(iterator2, sentinel)

        if value1 is sentinel and value2 is sentinel:
            break

        yield value1, value2

string = "abcd"
numbers = (10, 20, 30, 40)

generator_result = custom_zip(string, numbers)

print(generator_result)
for item in generator_result:
    print(item)

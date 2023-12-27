def custom_sum(*args):
    total_sum = 0
    for arg in args:
        if isinstance(arg, list):
            total_sum += custom_sum(*arg)
        else:
            total_sum += arg
    return total_sum

result1 = custom_sum([[1, 2, [3]], [1], 3])
print(result1)

result2 = custom_sum(1, 2, 3, 4, 5)
print(result2)

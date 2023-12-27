def tpl_sort(tpl):
    if all(isinstance(num, int) for num in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl

tpl = (6, 3, -1, 8, 4, 10, -5)
result = tpl_sort(tpl)
print(result)

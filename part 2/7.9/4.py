import random

# Способ 1: С использованием цикла
original_list = [i for i in range(10)]
paired_list_1 = [(original_list[i], original_list[i + 1]) for i in range(0, len(original_list), 2)]
print("Новый список (способ 1):", paired_list_1)

# Способ 2: С использованием zip и итератора
iter_original = iter(original_list)
paired_list_2 = list(zip(iter_original, iter_original))
print("Новый список (способ 2):", paired_list_2)
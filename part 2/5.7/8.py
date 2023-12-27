def is_cyclic_shift(str1, str2):
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        shifted_str = str2[i:] + str2[:i]
        if shifted_str == str1:
            return True, i

    return False, 0

input_str1 = input("Первая строка: ")
input_str2 = input("Вторая строка: ")

result, shift_value = is_cyclic_shift(input_str1, input_str2)
if result:
    print(f"Первая строка получается из второй со сдвигом {shift_value}.")
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")

def reverse_sequence_between_h(input_string):
    first_h_index = input_string.index('h')
    last_h_index = input_string.rindex('h')

    reversed_sequence = input_string[first_h_index + 1:last_h_index][::-1]

    return reversed_sequence

user_input = input("Введите строку: ")

if user_input.count('h') >= 2:
    result = reverse_sequence_between_h(user_input)
    print(f"Развёрнутая последовательность между первым и последним h: {result}")
else:
    print("Введенная строка не содержит как минимум двух букв 'h'.")

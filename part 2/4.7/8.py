def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()

            shifted_char = chr((ord(char) - ord('A' if is_upper else 'a') + shift) % 26 + ord('A' if is_upper else 'a'))

            result += shifted_char
        else:
            result += char

    return result

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = caesar_cipher(message, shift)
print("Зашифрованное сообщение:", encrypted_message)

encrypted_message = input("Введите зашифрованное сообщение: ")

decrypted_message = ''

start_half = ''
end_half = ''

i = 0
for letter in encrypted_message:
    if (i % 2 == 0):
        start_half += letter
    else:
        end_half = letter + end_half
    i += 1

decrypted_message = start_half + end_half

print("Расшифрованное сообщение:", decrypted_message)

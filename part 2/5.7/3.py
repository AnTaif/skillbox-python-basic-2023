def check_filename(filename):
    # Проверка начала файла
    disallowed_start_chars = ['@', '№', '$', '%', '^', '&', '*', '(']
    if filename[0] in disallowed_start_chars:
        return "Ошибка: название начинается недопустимым символом."

    allowed_extensions = ['.txt', '.docx']
    if not filename.endswith(tuple(allowed_extensions)):
        return "Ошибка: неверное расширение файла. Ожидалось .txt или .docx."

    return "Файл назван верно."

filename = input("Название файла: ")

result = check_filename(filename)
print(result)

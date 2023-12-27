import os

def calculate_directory_size(directory):
    total_size = 0
    total_files = 0
    total_directories = 0

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
            total_files += 1

        total_directories += 1

    return total_size, total_files, total_directories

directory_path = input("Введите путь до каталога: ")

size, files, directories = calculate_directory_size(directory_path)
size_kb = size / 1024

print(f"Размер каталога (в Кбайтах): {size_kb}")
print(f"Количество подкаталогов: {directories}")
print(f"Количество файлов: {files}")

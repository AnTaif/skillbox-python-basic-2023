import os

def gen_files_path(target_directory='/', user_specified_directory=''):
    file_paths = []

    for root, dirs, files in os.walk(target_directory):
        if user_specified_directory in dirs:
            user_directory_path = os.path.join(root, user_specified_directory)
            for dirpath, dirnames, filenames in os.walk(user_directory_path):
                file_paths.extend([os.path.join(dirpath, file) for file in filenames])
            break

    return file_paths

user_directory = input("Введите имя целевого каталога: ")
files_in_user_directory = gen_files_path(user_specified_directory=user_directory)

if files_in_user_directory:
    print(f"Файлы в каталоге {user_directory}:")
    for file_path in files_in_user_directory:
        print(file_path)
else:
    print(f"Каталог {user_directory} не найден.")

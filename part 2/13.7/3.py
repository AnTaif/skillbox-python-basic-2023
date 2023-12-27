import os

def count_lines_in_python_files(directory='.'):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    line_count = 0
                    in_comment_block = False

                    for line in file:
                        line = line.strip()

                        if not line or line.startswith('#'):
                            continue

                        if line.startswith("'''") or line.startswith('"""'):
                            in_comment_block = not in_comment_block

                        if not in_comment_block:
                            line_count += 1

                    yield f"{file_path}: {line_count}"

directory_path = input("Введите путь к директории (по умолчанию - текущая директория): ") or '.'
for result in count_lines_in_python_files(directory_path):
    print(result)

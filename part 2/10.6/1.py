import os

def process_names_file(file_path, error_log_path=None):
    total_characters = 0

    with open(file_path, 'r') as file:
        for line_number, name in enumerate(file, start=1):
            name = name.strip()
            name_length = len(name)
            
            if name_length < 3:
                error_message = f"Ошибка: менее трёх символов в строке {line_number}."
                print(error_message)

                if error_log_path:
                    with open(error_log_path, 'a', encoding='utf-8') as error_log:
                        error_log.write(error_message + '\n')

            total_characters += name_length

    return total_characters


if __name__ == "__main__":
    base_path = os.path.dirname(os.path.abspath(__file__))
    names_file_path = os.path.join(base_path, "people.txt")
    error_log_path = os.path.join(base_path, "errors.log")

    try:
        total_characters = process_names_file(names_file_path, error_log_path)
        print(f"Общее количество символов: {total_characters}")

    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

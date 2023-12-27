import os

def error_log_generator(log_file_path):
    with open(log_file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line

def filter_errors(input_file_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for error_line in error_log_generator(input_file_path):
            output_file.write(error_line)

input_log_file_path = input("Введите путь к файлу с логами: ")
output_log_file_path = input("Введите путь к файлу для записи ошибок: ")

filter_errors(input_log_file_path, output_log_file_path)

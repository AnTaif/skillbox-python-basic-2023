import os

path = os.path.dirname(os.path.abspath(__file__))
numbers_path = os.path.join(path, 'numbers.txt')
answer_path = os.path.join(path, 'answer.txt')

with open(numbers_path, 'r') as input_file:
    numbers = [int(line.strip()) for line in input_file if line.strip()]

sum_of_numbers = sum(numbers)

with open(answer_path, 'w') as output_file:
    output_file.write(str(sum_of_numbers))

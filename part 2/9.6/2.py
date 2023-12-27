path = os.path.dirname(os.path.abspath(__file__))
zen_path = os.path.join(path, 'zen.txt')

with open(zen_path, 'r') as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())
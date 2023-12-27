class SafeFile:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file is not None:
            self.file.close()

        return True

base_path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(base_path, "example.txt")

with SafeFile(filename, 'r') as file:
    content = file.read()
    print(content)
import os

base_path = os.path.dirname(os.path.abspath(__file__))

def validate_and_log(line):
    try:
        name, email, age = line.split()

        if not name or not email or not age:
            raise IndexError("НЕ присутствуют все три поля")

        if not name.isalpha():
            raise NameError("Поле «Имя» содержит НЕ только буквы")

        if '@' not in email or '.' not in email:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")

        age = int(age)
        if not 10 <= age <= 99:
            raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")

        return True

    except (IndexError, NameError, SyntaxError, ValueError) as e:
        with open(os.path.join(base_path, "registrations_bad.log"), "a") as bad_file:
            bad_file.write(f"{line.rstrip()}        {str(e)}\n")
        return False

with open(os.path.join(base_path, "registrations.txt"), "r") as input_file:
    for line in input_file:
        if validate_and_log(line):
            with open(os.path.join(base_path, "registrations_good.log"), "a") as good_file:
                good_file.write(line)

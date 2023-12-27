class Student:
    def __init__(self, full_name, group_number, grades):
        self.full_name = full_name
        self.group_number = group_number
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

students_data = [
    ("Студент 1", "А", [85, 90, 92, 88, 87]),
    ("Студент 2", "Б", [78, 80, 75, 82, 79]),
    ("Студент 3", "В", [92, 88, 90, 95, 87]),
]

students = [Student(name, group, grades) for name, group, grades in students_data]

sorted_students = sorted(students, key=lambda student: student.average_grade())

for student in sorted_students:
    print(f"{student.full_name}, Группа: {student.group_number}, Средний балл: {student.average_grade()}")

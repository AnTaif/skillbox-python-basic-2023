students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def get_student_info(student_dict):
    id_age_pairs = [(id, info['age']) for id, info in student_dict.items()]
    
    all_interests = set()
    total_surnames_length = 0
    
    for info in student_dict.values():
        all_interests.update(info['interests'])
        total_surnames_length += len(info['surname'])
    
    return id_age_pairs, all_interests, total_surnames_length

id_age_pairs, all_interests, total_surnames_length = get_student_info(students)

print(f"Список пар «ID студента — возраст»: {id_age_pairs}")
print(f"Полный список интересов всех студентов: {all_interests}")
print(f"Общая длина всех фамилий студентов: {total_surnames_length}")

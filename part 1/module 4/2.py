lang_result = int(input("Введите количество баллов по русскому языку: "))
math_result = int(input("Введите количество баллов по математике: "))
it_result = int(input("Введите количество баллов по информатике: "))

result = lang_result + math_result + it_result

if (result >= 270):
    print("Поздравляю, ты поступил на бюджет!")
else:
    print("К сожалению, ты не прошёл на бюджет.")

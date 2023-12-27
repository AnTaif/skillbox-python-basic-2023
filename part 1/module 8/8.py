boys = int(input("Введите количество мальчиков: "))
girls = int(input("Введите количество девочек: "))

seating = ""
diff = abs(boys - girls)

if (boys > 2 * girls) or (girls > 2 * boys):
    print("Ответ: Нет решения")
elif boys >= girls:
    for i in range(diff):
        seating += 'BGB'

    for j in range(girls - diff):
        seating += 'BG' 
else:
    for i in range(diff):
        seating += 'GBG'

    for j in range(boys - diff):
        seating += 'GB' 

print("Ответ:", seating)

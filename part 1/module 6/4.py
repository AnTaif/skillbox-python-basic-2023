likes = 0
dislikes = 0

while (True):
    rating = int(input("Введите оценку: "))
    if (rating == 0) :
        break

    if (rating > 0):
        likes += 1
    else:
        dislikes += 1

print("Кол-во положительных оценок:", likes)
print("Кол-во отрицательных оценок:", dislikes)

visitor_dice = int(input("Кубик Кости: "))
owner_dice = int(input("Кубик владельца: "))

if (visitor_dice >= owner_dice):
    difference = visitor_dice - owner_dice
    print(f"Разность: {difference}")
    print("Игрок платит")
else:
    total = visitor_dice + owner_dice
    print(f"Сумма: {total}")
    print("Владелец платит")

print("Игра окончена")

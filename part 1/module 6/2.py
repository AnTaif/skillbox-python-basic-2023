debt = 100
repayment = 0

print(f"Василий, ваша задолженность составляет {debt} рублей.")

while True:
    repayment = int(input("Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? "))
    if (repayment < debt):
        print("Маловато, Василий. Давайте ещё раз.")
        continue
    else:
        print("Отлично, Василий! Вы погасили долг. Спасибо!")
        break

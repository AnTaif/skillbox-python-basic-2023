euro_price = float(input("Введите стоимость покупки в евро: "))

dollars_price = euro_price * 1.25
rubles_price = dollars_price * 60.87

print(f"Стоимость покупки в рублях: {rubles_price:.2f} руб.")

user_input = input("Введите стоимости трех товаров через пробел: ")

prices = list(map(int, user_input.split()))
total_price = sum(prices)

discount = 10
final_price = total_price

if (total_price > 10000):
    final_price = total_price - (total_price * discount) / 100

print(f"Итоговая сумма: {final_price}")

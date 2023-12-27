def process_orders():
    n = int(input("Введите количество заказов: "))
    orders = {}

    for _ in range(n):
        order_info = input("Введите информацию о заказе (Фамилия Имя Пицца Количество): ").split()
        customer = f"{order_info[0]} {order_info[1]}"
        pizza = order_info[2]
        quantity = int(order_info[3])

        if customer not in orders:
            orders[customer] = {}

        if pizza not in orders[customer]:
            orders[customer][pizza] = quantity
        else:
            orders[customer][pizza] += quantity

    return orders

def print_customer_orders(orders):
    customers_sorted = sorted(orders.keys())
    
    for customer in customers_sorted:
        print(f"{customer}:")
        pizzas_sorted = sorted(orders[customer].keys())
        
        for pizza in pizzas_sorted:
            print(f"{pizza}: {orders[customer][pizza]}")

customer_orders = process_orders()

print_customer_orders(customer_orders)

def calculate_details_cost(shop, detail_name):
    count = 0
    total_cost = 0

    for detail in shop:
        if detail[0] == detail_name:
            count += 1
            total_cost += detail[1]

    return count, total_cost

shop = [
    ['каретка', 1200], 
    ['шатун', 1000], 
    ['седло', 300], 
    ['педаль', 100], 
    ['седло', 1500], 
    ['рама', 12000], 
    ['обод', 2000], 
    ['шатун', 200], 
    ['седло', 2700]
]

detail_name = input("Название детали: ")

total_count, total_cost = calculate_details_cost(shop, detail_name)
print(f"Общее количество деталей '{detail_name}': {total_count}")
print(f"Общая стоимость: {total_cost}")

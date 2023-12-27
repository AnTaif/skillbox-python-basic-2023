stall_statuses = input("Введите информацию о стойлах (a - свободное, b - занятое): ")

current_production = 2
total_milk = 0

for stall_status in stall_statuses:
    if (stall_status == 'b'):
        total_milk += current_production    
    current_production += 2

print(f"За день произведено {total_milk} л. молока")

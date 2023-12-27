num_graphics_cards = int(input("Количество видеокарт: "))

all_graphics_cards = []
old_graphics_cards = []

for i in range(num_graphics_cards):
    model = int(input(f"Видеокарта {i + 1}: "))
    all_graphics_cards.append(model)

max_value = max(all_graphics_cards)

old_graphics_cards = [x for x in all_graphics_cards if x != max_value]

print("")
print("Старый список видеокарт:", all_graphics_cards)
print("Новый список видеокарт:", old_graphics_cards)

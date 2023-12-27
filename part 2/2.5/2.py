names = ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]

even_names = []
for i, name in enumerate(names):
    if i % 2 == 0:
        even_names.append(name)

print("Первый день:", even_names)

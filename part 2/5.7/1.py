def display_menu(menu_string):
    menu_items = menu_string.split(';')

    displayed_menu = ', '.join(menu_items)

    return displayed_menu

menu_input = input("Доступное меню: ")

result = display_menu(menu_input)
print("Сейчас в меню есть:", result)

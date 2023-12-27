import copy

def create_website(product_name, base_site):
    new_site = copy.deepcopy(base_site)

    new_site['html']['head']['title'] = f'Куплю/продам {product_name} недорого'

    new_site['html']['body']['h2'] = f'У нас самая низкая цена на {product_name}'

    return new_site

def print_all_websites(websites):
    for i, site in enumerate(websites, start=1):
        print(f"Сайт для продукта {i}:")
        print(site)

base_site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

websites = []

num_websites = int(input("Сколько сайтов: "))

for _ in range(num_websites):
    product_name = input("Введите название продукта для нового сайта: ")
    new_site = create_website(product_name, base_site)
    websites.append(new_site)

    print_all_websites(websites)

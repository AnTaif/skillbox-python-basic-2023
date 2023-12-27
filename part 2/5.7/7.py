def is_valid_ip(ip):
    try:
        parts = ip.split('.')

        if len(parts) != 4:
            raise ValueError("Адрес — это четыре числа, разделённые точками.")

        for part in parts:
            num = int(part)
            if num < 0 or num > 255:
                raise ValueError(f"{num} превышает 255.")

        return True

    except ValueError as e:
        print(e)
        return False

input_ip = input("Введите IP: ")

if is_valid_ip(input_ip):
    print("IP-адрес корректен.")
else:
    print("IP-адрес некорректен.")

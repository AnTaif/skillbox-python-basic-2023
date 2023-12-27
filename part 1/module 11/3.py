import math

file_size = int(input("Укажите размер файла для скачивания в Мб: "))
download_speed = int(input("Какова скорость вашего соединения в Мб/сек: "))

remaining_size = file_size
time_elapsed = 0

while remaining_size > 0:
    downloaded = min(download_speed, remaining_size)
    remaining_size -= downloaded
    time_elapsed += 1
    percentage = math.ceil((1 - (remaining_size / file_size)) * 100)
    print(f"Прошло {time_elapsed} сек. Скачано {file_size - remaining_size} из {file_size} Мб ({percentage}%)")

print("Скачивание завершено.")

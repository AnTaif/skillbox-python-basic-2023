violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

def calculate_total_duration(selected_songs):
    total_duration = sum(violator_songs[song] for song in selected_songs)
    return total_duration

num_of_songs = int(input("Сколько песен выбрать? "))

selected_songs = []
for i in range(num_of_songs):
    song_name = input(f"Название {i + 1}-й песни: ")
    selected_songs.append(song_name)

total_duration = calculate_total_duration(selected_songs)
print(f"Общее время звучания песен: {total_duration:.2f} минуты")

import random

team1 = [round(random.uniform(5, 10), 2) for _ in range(20)]
team2 = [round(random.uniform(5, 10), 2) for _ in range(20)]

print(f"Первая команда: {team1}")
print(f"Вторая команда: {team2}")

winners = [max(score1, score2) for score1, score2 in zip(team1, team2)]

print(f"Победители тура: {winners}")

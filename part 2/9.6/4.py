def process_first_tour(input_file, output_file):
    with open(input_file, 'r') as f:
        k = int(f.readline().strip())
        participants = [line.strip().split() for line in f]

    second_tour_participants = [(name[0] + '. ' + name[1], int(score)) for name, score in participants if int(score) > k]
    second_tour_participants.sort(key=lambda x: x[1], reverse=True)

    with open(output_file, 'w') as f:
        f.write(f"{len(second_tour_participants)}\n")
        for i, (name, score) in enumerate(second_tour_participants, start=1):
            f.write(f"{i}) {name} {score}\n")

path = os.path.dirname(os.path.abspath(__file__))
first_path = os.path.join(path, "first_tour.txt")
second_path = os.path.join(path, "second_tour.txt")

process_first_tour(first_path, second_path)
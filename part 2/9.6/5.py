def frequency_analysis(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read().lower()

    letter_count = {letter: text.count(letter) for letter in set(text) if letter.isalpha()}
    total_letters = sum(letter_count.values())

    sorted_letters = sorted(letter_count.items(), key=lambda x: (-x[1], x[0]))

    with open(output_file, 'w') as file:
        for letter, count in sorted_letters:
            frequency = count / total_letters
            file.write(f"{letter} {frequency:.3f}\n")

path = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(path, "text.txt")
analysis_path = os.path.join(path, "analysis.txt")

frequency_analysis(text_path, analysis_path)
def count_oscillations(initial_amplitude, stopping_amplitude):
    if initial_amplitude <= stopping_amplitude:
        return 0

    count = 0
    while initial_amplitude > stopping_amplitude:
        initial_amplitude *= 0.916
        count += 1

    return count

initial_amplitude = float(input("Введите начальную амплитуду: "))
stopping_amplitude = float(input("Введите амплитуду остановки: "))

result = count_oscillations(initial_amplitude, stopping_amplitude)

print(f"\nМаятник остановился через {result} колебаний.\n")

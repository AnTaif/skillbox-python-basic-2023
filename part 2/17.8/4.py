from collections import Counter

def count_unique_characters(s):
    unique_count = sum(1 for var in Counter(s.lower()).values() if var == 1)
    return unique_count

message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)

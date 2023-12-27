from collections import Counter

def can_be_poly(s):
    char_count = Counter(s)
    odd_count = sum(count % 2 for count in char_count.values())

    return odd_count <= 1

print(can_be_poly('abcba'))  # True
print(can_be_poly('abbbc'))  # False

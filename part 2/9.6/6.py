import zipfile
import os
from collections import Counter

def extract_zip(zip_file, extract_path):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_path)

def count_letters(text):
    letter_count = Counter(text)
    return letter_count

def display_letter_statistics(letter_count, sort_order='desc'):
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=(sort_order == 'desc'))

    for letter, count in sorted_letters:
        print(f"{letter}: {count}")

path = os.path.dirname(os.path.abspath(__file__))

zip_file_path = os.path.join(path, "voina-i-mir.zip")
extraction_path = os.path.join(path, "extracted_text")
text_file_path = os.path.join(extraction_path, "voina-i-mir.txt")

extract_zip(zip_file_path, extraction_path)

with open(text_file_path, 'r', encoding='utf-8') as file:
    text_content = file.read()

letter_count = count_letters(text_content)
display_letter_statistics(letter_count, sort_order='desc')

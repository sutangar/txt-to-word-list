import re
from collections import Counter


def load_known_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        known_words = file.read().splitlines()
    return set(known_words)


def count_words(text_file_path, known_words_file_path):
    known_words = load_known_words(known_words_file_path)

    with open(text_file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r'\b\w+\b', text)
        words = [word for word in words if word not in known_words]
        word_counts = Counter(words)
        sorted_word_counts = sorted(word_counts.items(), key=lambda pair: pair[1], reverse=True)

        for word, count in sorted_word_counts:
            print(f"{word}: {count}")


text_file_path = 'your_text_file_path.txt'  # 请将此处替换为你的txt文件路径
known_words_file_path = 'your_known_words_file_path.txt'  # 请将此处替换为你的已知词汇txt文件路径
count_words(text_file_path, known_words_file_path)

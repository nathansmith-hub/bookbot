from collections import Counter

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def get_sorted_dict(char_counts):
    counts = list(char_counts.items())
    counts.sort(key=lambda count: count[1], reverse=True)
    return [{k: v} for k, v in counts]
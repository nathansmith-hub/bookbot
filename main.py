import sys

from stats import (
    get_num_words,
    get_char_count,
    get_sorted_dict
)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    dict_list = get_sorted_dict(char_count)
    print_report(book_path, num_words, dict_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_report(book_path, num_words, dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        key = next(iter(d))
        value = d[key]
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")

main()
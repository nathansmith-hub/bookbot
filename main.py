from stats import get_num_words, get_char_count, get_sorted_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    dict_list = get_sorted_dict(char_count)
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

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
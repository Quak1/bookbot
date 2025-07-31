import sys
from stats import (
    get_num_words, 
    get_char_count, 
    get_sorted_char_list
)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def report(file_path, num_words, sorted_char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for entry in sorted_char_count:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    text = get_book_text(file_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_char_count = get_sorted_char_list(char_count)

    report(file_path, num_words,sorted_char_count)


main()

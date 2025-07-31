def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    print(text)

main()

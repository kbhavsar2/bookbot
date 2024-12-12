def main():
    book_path = "books/frankenstein.txt"
    book_text = read_book(book_path)
    print(book_text)

def read_book(bp):
    with open(bp) as f:
        file_contents = f.read()
    return file_contents

main()
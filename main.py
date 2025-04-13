from stats import *

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_text(filepath)
    print(number_of_words(text))

if __name__ == "__main__":
    main()

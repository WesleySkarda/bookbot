from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
    return book_contents

def main():
    try:
        filepath = sys.argv[1]
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(filepath)
    number_of_words_var = number_of_words(text)
    repeting_character_var = sort_dictonary(repeting_character(text))
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(number_of_words_var)
    print("--------- Character Count -------")
    for item in repeting_character_var:
        if item.isalpha():
            print(f"{item}: {repeting_character_var[item]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()

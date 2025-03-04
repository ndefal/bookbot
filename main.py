import sys
from stats import wordcount
from stats import charcount
from stats import sort_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
      
    size = wordcount(book)
    letter_count = charcount(book)
    sorted_count = sort_letters(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {size} total words")
    print("--------- Character Count -------")
    
    for item in sorted_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")
    


main()
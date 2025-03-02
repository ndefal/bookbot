from stats import wordcount
from stats import charcount
from stats import sort_letters

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    
    size = wordcount(book)
    letter_count = charcount(book)
    sorted_count = sort_letters(letter_count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {size} total words")
    print("--------- Character Count -------")
    
    for item in sorted_count:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")
    


main()
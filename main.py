from stats import wordcount

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    book = get_book_text("books/frankenstein.txt")
    
    size = wordcount(book)

    print(f"{size} words found in the document")

main()
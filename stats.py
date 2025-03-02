def wordcount(book):
    split = book.split()
    return len(split)

def charcount(book):
    letter_count = {}
    lower_case = book.lower()
    
    for letter in lower_case:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count

def sort_on(dict):
    return dict["count"]

def sort_letters(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        char_dict = {'char' : char, 'count' : count}
        sorted_list.append(char_dict)
    
    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list

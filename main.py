def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_num_characters(text)



def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as book:
        return book.read()

def get_num_characters(text):
    lowered_string = text.lower()
    character_list = {

    }

    for character in lowered_string:
        if character in character_list:
            character_list[character] += 1
        else: 
            character_list[character] = 1

    print (character_list)


main()
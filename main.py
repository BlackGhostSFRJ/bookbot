def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    get_num_characters(text)

def sort_on(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as book:
        return book.read()

def get_num_characters(text):
    lowered_string = text.lower()
    list_of_characters = [

    ]
    character_dictionary = {

    }
    for character in lowered_string:
        if character in character_dictionary and character.isalpha():
            character_dictionary[character] += 1
        elif character not in character_dictionary and character.isalpha(): 
            character_dictionary[character] = 1

    for i in character_dictionary:
        list_of_characters.append(i)
        list_of_characters.append(character_dictionary[i])

    print (list_of_characters)


main()
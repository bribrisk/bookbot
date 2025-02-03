def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_character_count(text)

    print(num_characters)

def get_character_count(text):
    lowercase_str = text.lower()
    character_dictionary = {} #define empty dictionary

    for i in lowercase_str:
        if i not in character_dictionary:
            character_dictionary[i] = 1
        else:
            character_dictionary[i] += 1

    return character_dictionary



def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()



main()


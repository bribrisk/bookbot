def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_character_count(text)
    sorted_list = sort_dictionary(get_character_count(text))

    #print aggregated report
    print(f"--- Begin report of {book_path} ---")
    print("")
    print(f"{num_words} found in the document")

    for dictionary in sorted_list:
        for key, value in dictionary.items():
            print(f"The '{key}' character was found {value} times.")
    
    print("")
    print("--- End report ---")

def sort_dictionary(dict): 
    dict_to_list = dict.items()
    list_alpha_only = []
    for char in dict_to_list:
        if char[0].isalpha():
            tuple_to_dict = {char[0]: char[1]}
            list_alpha_only.append(tuple_to_dict)
    
    list_alpha_only.sort(reverse=True, key=lambda x: list(x.values())[0]) #the key=lambda accesses the value from each dictionary within the list
    
    return list_alpha_only


def get_character_count(text): #counts how many times each character appears
    lowercase_str = text.lower()
    character_dictionary = {} #define empty dictionary

    for i in lowercase_str:
        if i not in character_dictionary:
            character_dictionary[i] = 1
        else:
            character_dictionary[i] += 1

    return character_dictionary

def get_num_words(text): #counts how many words
    words = text.split()
    return len(words)

def get_book_text(path): #reads the text
    with open(path) as f:
        return f.read()



main()


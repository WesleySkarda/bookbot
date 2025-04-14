def number_of_words(text):
    return f"Found {len(text.split())} total words"

def repeting_character(text):
    character_dict = {}
    for letter in text.lower():
        if letter in character_dict:
            character_dict[letter] += 1
        else:
            character_dict[letter] = 1
    del character_dict[' ']
    del character_dict['\n']
    return character_dict

def sort_dictonary(dictonary):
    return dict(sorted(dictonary.items(), key=lambda item: item[1], reverse=True))
    
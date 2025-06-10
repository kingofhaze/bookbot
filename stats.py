def get_book_text(file):
    with open(file, 'r') as f:
        # Read the entire content of the file
        text = f.read()
        return text
    
def get_book_word_count(text):
    return len(text.split())

def get_book_character_count(text):
    # Count the number of characters to a dictionary character => count
    char_count = {}
    for char in text:
        lowered = char.lower()

        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1

    return char_count   

def get_book_character_count_sorted(counts):
    list_counts = []

    # Oragnize the characters as list of dictionaries name, count
    for char in counts:
        list_counts.append({'char': char, 'num': counts[char]})
    
    # Sort the list by count
    list_counts.sort(key=lambda x: x['num'], reverse=True)

    return list_counts
from stats import get_book_text, get_book_word_count, get_book_character_count, get_book_character_count_sorted

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_word_count(text)} total words")
    print("--------- Character Count -------")
    character_counts = get_book_character_count(text)
    sorted_counts = get_book_character_count_sorted(character_counts)
    
    for char in sorted_counts:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")

    print("============= END ===============")

if __name__ == "__main__":
    # This ensures that main() is called when the script is run directly
    main();
 
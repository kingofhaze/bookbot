from stats import get_book_text, get_book_word_count, get_book_character_count, get_book_character_count_sorted

def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_word_count(text)} total words")
    print("--------- Character Count -------")
    print(f"{get_book_character_count(text)}")
    print("=================================")
    print("Sorted")
    print(f"{get_book_character_count_sorted(text)}")

if __name__ == "__main__":
    # This ensures that main() is called when the script is run directly
    main();
 
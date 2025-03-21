from stats import count_words, count_characters, create_character_list_of_dicts
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read(), filepath

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {get_book_text(filepath)[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(filepath)[0])} total words")
    print("--------- Character Count -------")

    sorted_character_list = create_character_list_of_dicts(count_characters(get_book_text(filepath)[0]))

    for entry in sorted_character_list:
        if entry['character'].isalpha():
            print(f"{entry['character']}: {entry['count']}")
        else:
            continue



main()
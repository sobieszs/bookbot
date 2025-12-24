# Import the `connect` function and `db_version` variable from the `database.py` file
import sys

from stats import dict_into_list, get_char_count, get_num_words, sort_on


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) == 2:
        book = get_book_text(sys.argv[1])
        num_words = get_num_words(book)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        char_count = get_char_count(book)
        list_of_dicts = dict_into_list(char_count)
        # print(list_of_dicts)
        list_of_dicts.sort(reverse=True, key=sort_on)
        print("--------- Character Count ------")
        for item in list_of_dicts:
            print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()

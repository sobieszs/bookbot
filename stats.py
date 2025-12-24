def get_num_words(file_contents):
    list_of_words = file_contents.split()
    num_words = len(list_of_words)
    return num_words


def get_char_count(file_contents):
    list_of_words = file_contents.split()
    char_count = {}

    for word in list_of_words:
        for char in word:
            char_lower = char.lower()
            if char_lower in char_count:
                char_count[char_lower] += 1
            else:
                char_count[char_lower] = 1
    return char_count


dict = {
    "t": 29493,
    "h": 19176,
    "e": 44538,
    "p": 5952,
    "r": 20079,
    "o": 24494,
    "j": 497,
    "c": 9011,
    "g": 5795,
    "u": 10111,
    "n": 23643,
    "b": 4868,
    "k": 1661,
    "f": 8451,
    "a": 25894,
    "s": 20360,
    "i": 23927,
    ";": 1350,
    ",": 5962,
    "m": 10206,
    "d": 16318,
    "y": 7756,
    "w": 7450,
    "l": 12306,
    "v": 3737,
    ".": 3121,
    "-": 173,
    ":": 211,
    "2": 19,
    "3": 15,
    "0": 18,
    "1": 91,
    "[": 2,
    "#": 1,
    "4": 12,
    "5": 12,
    "]": 2,
    "&": 5,
    "8": 24,
    "/": 8,
    "*": 97,
    "’": 144,
    "x": 691,
    "_": 124,
    "q": 325,
    "?": 208,
    "—": 123,
    "6": 9,
    "z": 235,
    "(": 35,
    ")": 35,
    "7": 18,
    "æ": 28,
    "!": 201,
    "“": 506,
    "”": 316,
    "9": 9,
    "ë": 2,
    "‘": 43,
    "â": 8,
    "ê": 7,
    "ô": 1,
    "™": 57,
    "•": 4,
    "%": 1,
    "$": 2,
}


def dict_into_list(items):
    list_of_dicts = []
    for key in items:
        key = {"char": key, "num": items[key]}
        list_of_dicts.append(key)

    return list_of_dicts


def sort_on(items):
    return items["num"]

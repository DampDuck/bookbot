# python
from stats import word_counter, character_dict

def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()


def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"{word_counter(text)} words found in the document")
    print(character_dict(text))


if __name__ == "__main__":
    main()
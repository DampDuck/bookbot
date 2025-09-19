# python
def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def word_counter(text):
    split_text = text.split()
    return len(split_text)
   

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(f"{word_counter(text)} words found in the document")

if __name__ == "__main__":
    main()
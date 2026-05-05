import sys
import re
from collections import Counter


class Book:
    def __init__(self, pathname):
        self.pathname = pathname
        with open(pathname, "r", encoding="utf-8", errors="replace") as f:
            self.text = f.read()

    # Function 1: count words
    def word_count(self):
        words = re.findall(r"[A-Za-z0-9']+", self.text.lower())
        return len(words)

    # Function 2: count lines
    def line_count(self):
        return len(self.text.splitlines())

    # Function 3: most common words
    def top_words(self, n=10):
        words = re.findall(r"[A-Za-z0-9']+", self.text.lower())
        return Counter(words).most_common(n)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} PATHNAME_TO_TEXT_BOOK")
        sys.exit(1)

    path = sys.argv[1]

    # Demonstrate the class by creating a Book object and calling its functions
    book = Book(path)

    print("Book pathname:", book.pathname)
    print("Line count:", book.line_count())
    print("Word count:", book.word_count())
    print("Top 10 words:")
    for word, count in book.top_words(10):
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()

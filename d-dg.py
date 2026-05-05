#!/usr/bin/env python3
# CS 131B - Custom Objects HW #12
# 4/27/26
# This program defines a Book class with some text processing functions.

class Book:
    """Hold a plain text book and do stuff with it."""

    def __init__(self, pathname):
        """Save the path and load the text."""
        self.pathname = pathname
        self.content = None   # puts the whole file text here
        self._load_file()

    def _load_file(self):
        """Read the whole file into self.content."""
        f = open(self.pathname, 'r', encoding='utf-8')
        self.content = f.read()
        f.close()   # closes method

    def word_count(self):
        """Return how many words are in the book."""
        # split on whitespace gives us "words"
        words_list = self.content.split()
        return len(words_list)

    def line_count(self):
        """Return number of lines in the book."""
        # using splitlines is easier than counting newlines
        lines = self.content.splitlines()
        return len(lines)

    def average_word_length(self):
        """Average characters per word. Return 0.0 if no words."""
        words = self.content.split()
        if len(words) == 0:
            return 0.0
        total = 0
        for w in words:
            total = total + len(w)
        # could also use sum() but this is clearer to me
        return total / len(words)

    # extra optional method 
    def unique_word_count(self):
        """Return number of distinct words (case‑sensitive)."""
        words = self.content.split()
        return len(set(words))

    def __repr__(self):
        """Make it look like Book('pathname') when printed."""
        return "Book('" + self.pathname + "')"


def main():
    """Test the class with the required Urantia file."""
    book_path = "/users/abrick/resources/urantia.txt"
    try:
        b = Book(book_path)
        print("\nAnalyzing:", b.pathname)
        print("Word count:     ", format(b.word_count(), ','))
        print("Line count:     ", b.line_count())
        print("Avg word length:", round(b.average_word_length(), 2), "characters")
        # uncomment below if you want to see unique word count
        # print("Unique words:   ", b.unique_word_count())
    except FileNotFoundError:
        print("Oops, couldn't find the file:", book_path)
    except Exception as err:
        print("Something went wrong:", err)


# detects if run directly or imported
if __name__ == '__main__':
    print("This program (" + __file__ + ") was invoked on the command line.")
    main()
else:
    print("This program (" + __file__ + ") was imported into a running Python process.")
# Week 14: Custom Objects
# Task: Define and demonstrate a class of Book objects with at least three functions useful for processing plain-text books whose pathname is passed as a command-line argument.
# Test with: /users/abrick/resources/urantia.txt
# Usage:     python3 book.py /users/abrick/resources/urantia.txt

import sys           # for sys.argv (command-line arguments)
import re            # for regular expressions used in word splitting
from collections import Counter  # convenient way to count word frequencies


class Book:
    """A class representing a plain-text book.
    The Book is constructed from a pathname; the file is read once at construction time and stored as a single string in self.text.
    Several methods then operate on that text:
      - word_count():   total number of words in the book
      - top_words(n):   the n most common words and their counts
      - find_phrase(p): every line that contains the phrase p
    """

    # __init__ runs automatically when a new Book is created, e.g. Book(path).
    # 'self' refers to the new instance; the other parameters are inputs.
    def __init__(self, pathname):
        # Save the pathname so __repr__ and error messages can show it
        self.pathname = pathname

        # Read the entire file into self.text. Using 'with' guarantees, the file is closed even if an error occurs during reading.
        # encoding='utf-8' matches the encoding most plain-text books use;
        # errors='ignore' silently skips any byte that can't be decoded, so a single bad byte doesn't crash construction of the Book.
        with open(pathname, encoding='utf-8', errors='ignore') as file:
            self.text = file.read()

        # \b\w+\b matches sequences of word characters bounded by word boundaries, which gives us "words" without surrounding punctuation.
        self.words = re.findall(r"\b\w+\b", self.text.lower())

    # __repr__ returns a string representation of the object. Python calls this automatically whenever a Book is printed or shown in the REPL.
    # Keeping it short and informative is a common convention.
    def __repr__(self):
        return f"Book(pathname={self.pathname!r}, words={len(self.words)})"

    # Method 1: word_count
    # Returns the total number of words in the book. Because we already built self.words in __init__, this is just len() of that list.
    def word_count(self):
        return len(self.words)

    # Method 2: top_words
    # Returns the n most common words in the book as a list of (word, count) tuples, sorted from most frequent to least.
    # Counter.most_common(n) does the sorting and slicing for us.
    def top_words(self, n=10):
        counter = Counter(self.words)   # builds {word: count} efficiently
        return counter.most_common(n)   # returns top-n as [(word, count), ...]

    # Method 3: find_phrase
    # Returns every line of the book that contains the given phrase. The search is case-insensitive so "Light" matches "light" and "LIGHT".
    # We split self.text on newlines so we get the original (cased) lines back, which is more useful for a reader than the lowercased version.
    def find_phrase(self, phrase):
        phrase_lower = phrase.lower()                 # compare in lowercase
        matches = []                                  # accumulate hits here
        for line in self.text.splitlines():           # iterate over each line
            if phrase_lower in line.lower():          # case-insensitive check
                matches.append(line)                  # keep original casing
        return matches


# The block below only runs when this file is executed directly(e.g. "python book.py somefile.txt"). If another program imports this file with "import book", the demo will NOT run, which is
# exactly the behavior we want for a reusable class.
if __name__ == '__main__':
    # Step 1: get the pathname from the command line
    try:
        pathname = sys.argv[1]
    except IndexError:
        print("Usage: python book.py <pathname>")
        sys.exit(1)

    # Step 2: try to construct a Book from the pathname
    # Wrap construction in a try/except so a missing or unreadable file produces a friendly message instead of a raw traceback.
    try:
        book = Book(pathname)
    except FileNotFoundError:
        print(f"File not found: {pathname}")
        sys.exit(1)
    except PermissionError:
        print(f"Permission denied: {pathname}")
        sys.exit(1)

    # Step 3: demonstrate that book is, in fact, a Book type() returns the class of an object; printing the book itself
    # invokes our __repr__ method.
    print("type(book):", type(book).__name__)
    print("repr(book):", repr(book))
    print()

    # Step 4: demonstrate each of the three methods

    # word_count() -- total number of words
    print(f"Total words: {book.word_count():,}")
    print()

    # top_words(n) -- most frequent words and their counts
    print("Top 10 most common words:")
    for word, count in book.top_words(10):
        # :>12 right-aligns the word in a 12-char field, :>6 the count;
        # this lines the output up neatly into two columns.
        print(f"  {word:>12}  {count:>6,}")
    print()

    # find_phrase(p) -- every line containing the phrase
    # We pick a phrase that's reasonably common in most books so the demo always produces some output, but cap the display at the first few hits so the screen doesn't fill with thousands of lines.
    phrase = "the universe"
    hits = book.find_phrase(phrase)
    print(f"Lines containing {phrase!r}: {len(hits):,} found")
    for line in hits[:3]:                 # show only the first 3 hits
        print(f"  > {line.strip()}")      # strip removes leading/trailing space
    if len(hits) > 3:
        print(f"  ... and {len(hits) - 3:,} more.")

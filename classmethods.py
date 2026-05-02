#!/usr/bin/env python3
import random
import re
import sys


class Book:
    def __init__(self, book_name_loc):
        match = re.search(r"^(?P<location>.*)/(?P<filename>[^/]+)$", book_name_loc)
        if not match:
            raise ValueError(f"Invalid path format: '{book_name_loc}'")
        self.location = match.group("location")
        self.filename = match.group("filename")
        self.book_name_loc = book_name_loc
        self._text = self._read_text()

    def _read_text(self):
        with open(self.book_name_loc, "r", encoding="utf-8") as file:
            return file.read()

    def count_unique_words(self):
        words = re.findall(r"[a-zA-Z]+", self._text.lower())
        return len(set(words))

    def largest_integer(self):
        numbers = re.findall(r"\d+", self._text)
        if not numbers:
            return None
        return max(int(value) for value in numbers)

    def random_long_words(self, count=10, min_length=10):
        words = re.findall(r"[a-zA-Z]+", self._text.lower())
        candidates = sorted({word for word in words if len(word) > min_length})
        if len(candidates) < count:
            raise ValueError(
                f"Only {len(candidates)} unique words longer than {min_length} characters were found."
            )
        return random.sample(candidates, count)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 classmethods.py <path_to_text_file>")
        sys.exit(1)

    file_name_and_location = sys.argv[1]

    try:
        book = Book(file_name_and_location)
    except FileNotFoundError:
        print(f"Error: file not found: '{file_name_and_location}'")
        sys.exit(1)
    except PermissionError:
        print(f"Error: permission denied for '{file_name_and_location}'")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: could not decode '{file_name_and_location}' as UTF-8 text")
        sys.exit(1)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"Error: unexpected problem reading input file: {error}")
        sys.exit(1)

    print(
        f"Input is a book named '{book.filename}' at location '{book.location}'."
    )
    print(f"Unique words: {book.count_unique_words()}")

    largest = book.largest_integer()
    if largest is None:
        print("Largest integer: none found")
    else:
        print(f"Largest integer: {largest}")

    try:
        words = book.random_long_words(count=10, min_length=10)
        print("10 random words over 10 characters:")
        for word in words:
            print(word)
    except ValueError as error:
        print(f"Random long words: {error}")


if __name__ == "__main__":
    main()
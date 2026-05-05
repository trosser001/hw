import sys
import re

class Book:
    def __init__(self, path):
        self.path = path

        with open(path) as file:
            self.text = file.read()

    def word_count(self):
        return len(re.findall(r"[A-Za-z]+", self.text))

    def unique_word_count(self):
        words = re.findall(r"[A-Za-z]+", self.text.lower())
        return len(set(words))

    def greatest_integer(self):
        numbers = re.findall(r"\d+", self.text)

        if len(numbers) == 0:
            return None

        return max(map(int, numbers))

    def __repr__(self):
        return "Book({})".format(self.path)


try:
    book = Book(sys.argv[1])

    print(book)
    print(book.word_count())
    print(book.unique_word_count())
    print(book.greatest_integer())

except IndexError:
    print("No filename passed.")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("File not readable.")
except UnicodeDecodeError:
    print("File is not encoded in UTF-8.")

import sys

class Book:
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            self.content = f.read()

    def word_count(self):
        return len(self.content.split())

    def unique_words(self):
        return set(self.content.split())

    def character_count(self):
        return len(self.content)

book = Book(sys.argv[1])

total_words = book.word_count()

print(f'The book contains {total_words} words.')

total_unique_words = len(book.unique_words())

print(f'The book contains {total_unique_words} unique words.')

total_characters = book.character_count()

print(f'The book contains {total_characters} characters.')
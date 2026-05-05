# This program defines and demonstrates a class of Book objects having at least three functions useful for processing the content of plain-text books whose pathname is passed as argument: /users/abrick/resources/urantia.txt

import sys

class Book:
	def __init__(self, text_path):
		self.text = open(text_path).read()		# Store the text content from the file into self.text
	def get_title(self):					# Function 1: get the book title
		lines = self.text.splitlines()
		return lines[0].strip()
	def count_words(self):					# Function 2: count the number of words in the book
		return len(self.text.split())
	def count_char(self):					# Function 3: count the number of characters in the book
		return len(self.text)

if __name__ == "__main__":
	try:
		text = sys.argv[1]
		book = Book(text)				# The object will open, read and store the text

		print(f"The title of the book: {book.get_title()}")
		print(f"Number of words in the book: {book.count_words()}")
		print(f"Number of characters in the book: {book.count_char()}")

	except FileNotFoundError:
        	print("File Not found.")
	except IsADirectoryError:
        	print("Invalid path.")
	except IndexError:
        	print("No file name passed.")


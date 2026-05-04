
import random
import re
import sys

# Assignment: Write a program that defines and demonstrates a class of Book objects having at least three functions useful for processing the content of plain-text books whose pathname is passed as argument. 
# Test with /users/abrick/resources/urantia.txt & peer review, both due 5/3

# Defines Book class (and I added code to use (create) Book objects and call the class methods...in the same program

# The class has methonds to read a book and count unique words, find the largest integer, and return 10 random long words
# made use of code from my other homework assignements and all the eye-opening code from reviewing all of our prior works/peer reviews.

class Book:
# The class object is initialized with the path to the book file and store it in a class attribute, self.book_text
    def __init__(self, book_name_loc):
        # The path to the book file is stored in the book_name_loc attribute
        self.book_name_loc = book_name_loc
        self.book_text = self.read_book()

    def read_book(self): # The book file is read and the text is stored in the book_text attribute- a memory hog, maybe. 
        with open(self.book_name_loc, "r", encoding="utf-8") as file:# open the book file and read the text
            return file.read()

    def count_unique_words(self):# The count_unique_words method counts the unique words in the book
        words = re.findall(r"[a-zA-Z]+", self.book_text.lower())# find all words in the book and convert to lowercase
        return len(set(words))# return the number of unique words using a set to remove duplicates

    def largest_integer(self):# The largest_integer method finds the largest integer in the book
        numbers = re.findall(r"\d+", self.book_text)# find all integers in the book
        if not numbers:
            return None
        return max(int(value) for value in numbers)# return the largest integer using a generator expression

    def random_long_words(self):# This method returns 10 random words each over 10 characters  from the book
        count=min_length=10# i was going to pass these as parameters, but i decided to hardcode them for now
        words = re.findall(r"[a-zA-Z]+", self.book_text.lower())# find all words in the book and convert to lowercase
        candidates = sorted({word for word in words if len(word) > min_length}) # sort the words by length using a set to remove duplicates...
        if len(candidates) < count:
            raise ValueError(# if there are less than 10 words, raise a ValueError, which is a built-in exception that is raised when a function encounters an error. This cleanly terminates the program.
                f"Only {len(candidates)} unique words longer than {min_length} characters were found."
            )
        return random.sample(candidates, count)


def main():
    if len(sys.argv) != 2:# if the number of arguments is not 2, print the usage message and exit the program
        print("Usage: python3 classmethods.py <path_to_text_file>")
        sys.exit(1)

    book_path = sys.argv[1]

    try:
        book = Book(book_path)  # create a Book object with the path to the book file
    except FileNotFoundError:# if the file is not found, print the error message and exit the program
        print(f"Error: file not found: '{book_path}'")
        sys.exit(1)
    except PermissionError:# the program doesn't have permission to read the file, print the error message and exit the program
        print(f"Error: permission denied for '{book_path}'")
        sys.exit(1)
    except UnicodeDecodeError:# the file is not encoded as UTF-8, print the error message and exit the program
        print(f"Error: could not decode '{book_path}' as UTF-8 text")
        sys.exit(1)
    except ValueError as error:# if there is a ValueError, which is a built-in exception that is raised when a function encounters an error. This cleanly terminates the program.
        print(f"Error: {error}")
        sys.exit(1)
    except Exception as error:# if there is any other error, print the error message and exit the program
        print(f"Error: unexpected problem reading input file: {error}")
        sys.exit(1)

    print(f"Input book path: '{book_path}'")
    print(f"Unique words: {book.count_unique_words()}")# print the number of unique words in the book using the class method count_unique_words

    largest = book.largest_integer()# find the largest integer in the book using the class method largest_integer
    if largest is None:# if the largest integer is not found, print the error message but don't kill the program
        print("Largest integer: none found")# print the error message
    else:# if the largest integer is found, print the largest integer using the class method largest_integer
        print(f"Largest integer: {largest}")# print the largest integer using the class method largest_integer

    try:
        words = book.random_long_words()
        print("10 random words over 10 characters:")
        for word in words:
            print(word)
    except ValueError as error:# if there is a valueerror in random_long_words, print the error message but don't kill the program
        print(f"Random long words: {error}")


if __name__ == "__main__":# if the script is run directly, call the main function
    main()
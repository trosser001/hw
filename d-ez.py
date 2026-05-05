import sys
import os

class Book:
    def __init__(self, pathname):
        """Initializes the Book object by reading the path argument[cite: 3]."""
        self.pathname = pathname
        self.filename = os.path.basename(pathname)
        
        # CPU processes the instruction to fetch data from Secondary Memory
        try:
            with open(pathname, 'r', encoding='utf-8') as f:
                self.content = f.read()
        except FileNotFoundError:
            self.content = None
            print(f"Error: The file '{pathname}' was not found.")
        except Exception as e:
            self.content = None
            print(f"An unexpected error occurred: {e}")

    def get_word_count(self):
        """Function 1: Returns total words using string splitting."""
        return len(self.content.split()) if self.content else 0

    def get_line_count(self):
        """Function 2: Returns total lines."""
        return len(self.content.splitlines()) if self.content else 0

    def count_word(self, target):
        """Function 3: Counts specific word occurrences (case-insensitive)."""
        if not self.content: return 0
        return self.content.lower().count(target.lower())

    def get_summary(self):
        """Function 4: Returns a quick stats summary string."""
        if self.content is None: return "No content to summarize."
        return f"{self.filename}: {len(self.content)} characters."

    def find_most_frequent_char(self):
        """Function 5: Iterates to find the most common character[cite: 4]."""
        if not self.content: return None
        char_counts = {}
        # Iterative logic to process content[cite: 4]
        for char in self.content.replace(" ", "").replace("\n", ""):
            char_counts[char] = char_counts.get(char, 0) + 1
        
        if not char_counts: return None
        return max(char_counts, key=char_counts.get)

    def __repr__(self):
        """Special method for object representation[cite: 3]."""
        return f"<Book Object: {self.filename}>"

# Main logic for Terminal Execution[cite: 4]
if __name__ == "__main__":
    # Check if a pathname argument was provided in the terminal
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <path_to_text_file>")
    else:
        # The first argument (index 1) is the pathname passed by the user
        target_path = sys.argv[1]
        my_book = Book(target_path)

        # Only proceed if the file was loaded successfully
        if my_book.content is not None:
            print("-" * 30)
            print(f"Processing: {my_book.filename}")
            print(f"1. Total Words: {my_book.get_word_count()}")
            print(f"2. Total Lines: {my_book.get_line_count()}")
            print(f"3. Occurrences of 'the': {my_book.count_word('the')}")
            print(f"4. Summary: {my_book.get_summary()}")
            print(f"5. Most Frequent Char: {my_book.find_most_frequent_char()}")
            print("-" * 30)

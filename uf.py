import re
import sys

def find_greatest_integer(path):
    """
    Scans the file for all digit sequences and tracks the largest numerical value.
    """
    # Initialize as None to distinguish between 'no numbers found' and the number 0
    greatest = None

    # Pre-compiling the pattern for performance as suggested in the notes.
    # r'\d+' looks for one or more (+) digits (\d).
    integer_pattern = re.compile(r'\d+')

    try:
        with open(path, 'r') as file:
            # Iterating line-by-line is efficient for large files.
            for line in file:
                # findall() extracts all digit sequences as strings
                matches = integer_pattern.findall(line)
                
                for s in matches:
                    # Convert the string match to an actual integer
                    current_num = int(s)
                    
                    # Update greatest if it's the first number seen or a new maximum
                    if greatest is None or current_num > greatest:
                        greatest = current_num
        
        return greatest

    except FileNotFoundError:
        sys.exit(f"Error: The file '{path}' was not found.")
    except Exception as e:
        sys.exit(f"An unexpected error occurred: {e}")

def main():
    # Verify that a command-line argument was provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <pathname>")
        sys.exit(1)

    pathname = sys.argv[1]
    
    # Execute the search
    result = find_greatest_integer(pathname)

    # Final Output
    if result is not None:
        print(f"The single greatest integer found in the text is: {result}")
    else:
        print("No integers were found in the file.")

if __name__ == "__main__":
    main()

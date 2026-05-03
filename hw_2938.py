import re
import sys

# assignment: Write a program that indicates the single greatest integer in the text whose pathname is passed as argument.
# Test with /users/abrick/resources/urantia.txt
# assumptions: numbers can include commas, and commas are removed before comparing values.

def greatest_integer_in_file(file_name_and_location):
    try:
        with open(file_name_and_location, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: file not found: '{file_name_and_location}'")
        return None
    except PermissionError:
        print(f"Error: permission denied for '{file_name_and_location}'")
        return None
    except IsADirectoryError:
        print(f"Error: expected a file but got a directory: '{file_name_and_location}'")
        return None
    except UnicodeDecodeError:
        print(f"Error: could not decode '{file_name_and_location}' as UTF-8 text")
        return None
    except Exception as e:
        print(f"Error: unexpected problem reading input file: {e}")
        return None

    # find number-like chunks such as 1,000 or 42
//  matches = re.findall(r"[\d,]+", text)
    num = r"[0-9]+"
    nums = re.findall(num, text)
    nums = [int(i) for i in nums]
    if not nums:
        return None
    return max(nums)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as an argument.")
        print("It should be run like this: python3 hw_2938.py /path/to/your/file.txt")
        sys.exit(1)

    file_name_and_location = sys.argv[1]
    result = greatest_integer_in_file(file_name_and_location)

    if result is None:
        print(f"Error: no integers were found in '{file_name_and_location}'.")
        sys.exit(1)

    print(f"The greatest integer in '{file_name_and_location}' is: {result}")

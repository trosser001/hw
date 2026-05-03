# CS131B - Week 13: Regular Expressions
# Task: Find the single greatest integer in a text file
# whose pathname is passed as a command-line argument.
#
# This week we learned to use the 're' module for pattern matching.
# Here we apply re.findall() to extract all integers from the file,
# then use max() to find the largest one.
#
# A raw string r'\d+' matches one or more consecutive digit characters,
# which is how we identify integers in the text.
#
# Test file: /users/abrick/resources/urantia.txt
# Usage: python greatest_integer.py /users/abrick/resources/urantia.txt
# =============================================================

import re   # the regular expressions module
import sys  # gives us access to sys.argv for command-line arguments

# --- Step 1: Get the filename from the command line ---
try:
    filename = sys.argv[1]          # sys.argv[1] is the first argument after the script name
except IndexError:
    print("No filename passed.")    # user forgot to provide a file path
    sys.exit(1)                     # exit with error code so the shell knows something went wrong

# --- Step 2: Open and read the file safely ---
try:
    with open(filename) as file:    # 'with' closes the file automatically when the block ends
        text = file.read()          # read entire file into one string
except FileNotFoundError:
    print("File not found.")        # the path does not exist
    sys.exit(1)
except PermissionError:
    print("File not readable.")     # OS denied access
    sys.exit(1)
except UnicodeDecodeError:
    print("File is not encoded in UTF-8.")  # file contains undecodable bytes
    sys.exit(1)

# --- Step 3: Extract all integers using a regular expression ---
# r'\d+' is a raw string pattern meaning "one or more digit characters"
# re.findall() returns a list of all non-overlapping matches as strings
matches = re.findall(r'\d+', text)  # e.g. ['1935', '42', '1000000', ...]

# --- Step 4: Check that we actually found some integers ---
if not matches:
    print("No integers found in the file.")
    sys.exit(1)

# --- Step 5: Convert matches from strings to integers and find the max ---
# findall() returns strings, so we must convert each to int before comparing
integers = [int(m) for m in matches]   # list comprehension: convert every match to int
greatest = max(integers)               # max() returns the largest value in the list

# --- Step 6: Report the result ---
print(f"The greatest integer found in '{filename}' is: {greatest}")

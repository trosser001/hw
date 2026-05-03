# Write a program that indicates the single greatest integer
# in the text whose pathname is passed as argument. 
# Test with /users/abrick/resources/urantia.txt

import sys
import re

def openfile(file_path):
    try:
        file = open(file_path)
        return file
    except:
        print(f"file {file_path} not found")
        sys.exit()

def get_filepath():
    try:
        file_path = sys.argv[1]
        return file_path
    except:
        print("No argument found. Syntax: script <file_path>")
        sys.exit()

def str2int(str):
    """ Helps catch what can't be converted by int(), such as '1,000'. """
    try:
        return int(str)
    except:
        print(f"could not convert {str} to int")
        sys.exit()

def clean_intstr(str: str):
    """ removes commas in input string """
    return str.replace(',','')

def extract_integers(file):
    """
    Input= file : text file containing word characters and posibly other characters.

    Return= matches : list of integers in the file
    
    Posible instances of integers include a whitespace character followed by
        \d\d\d\d...     - i.e. a series of digits.
        \d,\d\d\d...    - 1, 2, or 3, digits followed by a comma and groups of 3 digits seperated by a comma.
        \[-+]\d...      - either of above forms with a leading '+' or '-' sign (negative integers)
    Some accepted edge cases:
        \d\d\d\. ...    - a number followed by a '.' and then a whitespace or end (assuming the end of a sentence).
    Notable exclutions:
        \d.\d\d\d       - decimals
        \d\/\d\d\/\d\d  - dates
        \(\d\d...\)     - a number inside parentheses
    """
    pattern = r"(?:(?<=\s)|(?<=^))[-+]?(?:\d{1,3}(?:,\d{3})*|\d+)(?=\s|$|[.,](?=\s|$))"
    try:
        int_strings = re.findall(pattern, file.read())
    except:
        print('Something went wrong.')
        sys.exit()
    
    integers = list( str2int(clean_intstr(str)) for str in int_strings)
    return integers

# main

# get file path argument
file_path = get_filepath()

# open the file
file = openfile(file_path)

# read and extract integers from the file
integers = extract_integers(file)

# print the first 20 integers
print(integers[:20])

# Return the largest integer
print(max(integers))

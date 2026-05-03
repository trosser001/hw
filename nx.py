# Write a program that indicates the single greatest integer in the text whose pathname is passed as argument. Test with /users/abrick/resources/urantia.txt

import re, sys

# try to open file and raise exceptions if errors occur
try:
    f = open(sys.argv[1])
except IndexError:
    print ('No filename passed.')
    exit()
except FileNotFoundError:
    print ('File not found.')
    exit()
except PermissionError:
    print ('File not readable.')
    exit()

# create re-useable function that identifies all unique integers
def unique_int(f):
    ints = set()
    for line in f:
        # in each line, identify match object where numbers exist
        line_ints = re.finditer(r"\d+", line)
        # extract number from match object, convert to integer and store
        for num in line_ints:
            ints.add(int(num.group()))
    return ints

# find greatest integer
int_set = unique_int(f)
greatest_int = max(int_set)
print(greatest_int)


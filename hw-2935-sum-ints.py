# I use this function I call from a compressed statement with sum, for each arg (exept the first) in sys.argv, to check and clean 
# each arg. It returns it as an INT value if it is one.  The returned value is summed.

# If the arg is not an int (a string other than a sting int, a float, the presence of any commas, or underscores, anything but an int), 
# the funct returns a zero and the 0 is added (it doesn't affect the sum of ints) 

import sys

def to_int(arg):
    try:
        # 1. First clean the string of commas, underscore and empty spaces:
        clean = arg.replace(",", "").replace("_", "").strip()
        # 2. Skip floats manually (since int("1.0") is a ValueError we want to ignore)
        if "." in clean: return 0
        # 3. Try the conversion
        return int(clean)
    except ValueError:
        # 4. If it's "True", "apple", etc., just return 0
        return 0

# One-liner (i call it a compressed statement) sum statement using the "to_int" function I defined above. 
total = sum(to_int(arg) for arg in sys.argv[1:])

print(f"Total Sum: {total}")

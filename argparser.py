import sys

# Use sum() with a generator expression to process batch arguments
total = sum(int(clean) for arg in sys.argv[1:] if (clean := arg.replace(",", "").replace("_", "").strip()) and "." not in clean ) 
print(f"Total Sum: {total}")
 
# 1. Clean commas, underscores, and surrounding whitespace
# 2. Ignore anything with a decimal point (floats)
# 3. Only keep it if it's numeric (handles negative sign via lstrip)


"""
def main():
    # Use only user-provided arguments, skipping argv[0]
    args = sys.argv[1:]

    # Trying to be as short with my code as possible. 
    total = sum(
        int(clean) 
        for arg in raw_args 
        if (clean := arg.replace(",", "")) and "." not in clean 
        and (clean.lstrip("-").isdigit())
    )

    print(f"Total Sum: {total}")

if __name__ == "__main__":
    main()


import sys
import argparse
found = list()
for argument in sys.argv[1:]:
	try:
		found.append(int(argument))
	except ValueError as e:
		pass

print(found, sum(found))

if len(found) == 0:
	raise TypeError('No argument was an integer.')

import sys

def main():
    # Capture only user-provided arguments, skipping argv[0]
    raw_args = sys.argv[1:]

    # A pythonic one-liner using sum() and a generator expression
    total = sum(
        int(clean) 
        for arg in raw_args 
        if (clean := arg.replace(",", "")) and "." not in clean 
        and (clean.lstrip("-").isdigit())
    )

    print(f"Total Sum: {total}")

if __name__ == "__main__":

# 1. Initialize the parser
parser = argparse.ArgumentParser(description="A simple greeting script.")
# With condition
evens = [x for x in range(100) if x % 10 == 0]
print(evens)
# 2. Add a positional (required) argument
parser.add_argument("name", help="The name of the person to greet")

# 3. Add an optional flag (boolean switch)
parser.add_argument("-g", "--greet", action="store_true", help="Include a 'Hello' greeting")

# 4. Parse the input
args = parser.parse_args()

# 5. Use the results
if args.greet:
    print(f"Hello, {args.name}!")
else:
    print(args.name)
"""

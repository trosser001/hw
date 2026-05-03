import sys
import re

if len(sys.argv) != 2:
    print("Need a file.")
    sys.exit()

try:
    text = open(sys.argv[1]).read()
except:
    print("Cannot open file.")
    sys.exit()

# find all numbers
numbers = re.findall(r'\d+', text)

biggest = 0

for num in numbers:
    num = int(num)
    if num > biggest:
        biggest = num

print(biggest)

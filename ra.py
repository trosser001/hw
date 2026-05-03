# Write a program that indicates the single greatest integer
# in the text whose pathname is passed as argument.
# Test with /users/abrick/resources/urantia.txt

import sys
import re

# Check if arg is passed
try:
        txt_file = open(sys.argv[1])
except IndexError:
        print('No filename passed.')
except FileNotFoundError:
        print('File not found.')
except PermissionError:
        print('File not readable.')

txt = txt_file.read()
txt_file.close()

txt_list = list(txt.split())
nums=[]
num_list=[]

# Find all of the numbers int the text, then add them to a list
for i in txt_list:
	nums = re.findall(r'\d+',i)
	for j in nums:
		num_list.append(int(j))

print(max((num_list)))



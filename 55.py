# Program that indicates the single greatest integer in the text whose pathname is passed as argument.
import sys
import re
greatest = 0
numbers = []
try:
 fname = sys.argv[1] #saves the name of the passed file
 fhand = open(fname) #tries to open the file
except IndexError: #closes program if a file is not given
 print('No file passed')
 sys.exit()
except: #keeping this general as I only care about whether the file can open
 print('File Error: File cannot be opened or does not exist', 'File name:',fname)
 sys.exit()
for line in fhand:
 line = line.rstrip() #removes trailing whitespace
 filter = re.findall('[0-9]+',line) #pulls out all numbers from the text per line
 if len(filter) > 0 : #saves the pulled numbers in a string as integers
  for num in filter:
   numbers.append(int(num))
#prints the single greatest integer in the text
print("The single greatest integer in the text is", str(max(numbers)))


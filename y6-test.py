# write a program that shows 10 unique random words,
# made only of letters, and over 10 letters long,
# that occur in the text whose pathname is passed as an arg

import sys
import string
import random

# open file, read, change letters to lowercase, and split into list
with open(sys.argv[1]) as myfile:
    words = myfile.read().lower().split()

# remove punctuation
words = [word.strip(string.punctuation) for word in words]

# keep only words that are made only of letters and are longer than 10 characters
words = [word for word in words if word.isalpha() and len(word) > 10]
#words = [word for word in words if len(word) > 10]

# change to set to remove duplicates, change back to list, and print 10
print(" ".join(random.sample(list(set(words)), 10)))
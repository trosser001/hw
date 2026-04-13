# Assignment: write a program that prints all unique command-line arguments
# it receives in alphabetical order, with no duplicates.

# I used slicing logic from Severance, Python for Everybody:
# Chapter 6, "Strings," section 6.4, "String slices" (page 69),
# and Chapter 8, "Lists," section 8.5, "List slices" (page 94).
#
# Severance explains that a slice written as [n:m] starts at index n
# and stops before index m. He also explains that if you leave off the
# second number, Python keeps going to the end of the sequence.
#
# sys.argv is a list, so sys.argv[1:] gives all command-line arguments
# from position 1 through the end, which skips sys.argv[0] because that
# first item is just the script name.

# Example:
#   [1:10] means start at index 1 and stop before index 10.
#   [1:]   means start at index 1 and go all the way to the end.

# Severance did not cover sets in the part I used for this assignment.
# I got the set idea from the YouTube video
# "Python Lists vs Tuples vs Sets - Visually Explained."
#
# The useful part here is that when you convert a list to a set,
# duplicate values are removed automatically.

# Example:
#   alist = ['a', 'b', 'c', 'a']
#   aset = set(alist)
#   sorted(aset) 
#   results in {'a', 'b', 'c'} the duplicate 'a' is removed.

# Then I can sort the remaining unique values into alphabetical order.

# So this assignment can be solved cleanly by combining:
#   1) sys.argv[1:]   to skip the script name
#   2) set(...)       to remove duplicates
#   3) sorted(...)    to put the results in alphabetical order

import sys

print(sorted(set(sys.argv[1:])))

#alist=['a', 'b', 'c', 'a']
#aset=set(alist)
#print(sorted(aset))

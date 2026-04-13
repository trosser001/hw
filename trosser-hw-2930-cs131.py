# Date:  March 8, 2026
#
# Requirement: Homework assignment for CS131B at CCSF; Write a program that prints out the exact command line arguments it receives, unchanged, 
# but reordered from last to first.



# Import of sys to gain access to parameters used when executing a python script
import sys

# Since the argv is mutable, moved into another list 'args', to preserve argv
args=sys.argv[:]

# The script name is actually one of the parameters.  It is auto-magically passed via sys.argv, and it is always located in index position [0]. This assigns the 
# argument with the script name to a variable to use later.  This is done to allow for a better looking sort of the arguments entered by the user.  
script_name=args[0]


# If the user entered no arguments ... the script name is still passed, so the first part of this if addresses that unique scenario, otherwise, the parameters 
# entered, are listed in reverse order, and THEN the script name is rendered.  Which is, in fact, in reverse order ;)

if len(args) == 1: 
	print("No arguments were entered by the user.  The only parameter received was the script name: ", script_name)
else:

# This else begins by removing args.pop(0) using the list pops method, which is script name from the args list, and makes it available in the 'script_name" variable.
# Once that is done, the 'sorted' method is used to reorder the remaing user entered arguments, and then the script name is listed, but seperated.  

	args.pop(0)
	print("The arguments passed, in reverse order, were:", sorted(args, reverse=False), "and the script name: ", script_name)

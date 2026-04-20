# for assignment to take in the number of sides on a die, and the number of rolls to perform, 
# and return the number of roll results where the face was a multiple of 10

# Assumptions:  Based on something I found on the internet, I am assuming only die with 2, 4, 6, 8, 12 and 20 faces are FAIR dice -
# but I am adding in 100 sides as valid also

# 		Any other values are rejected, and program terminates.

# April 14, 2026: per Peer Reviews, I have changed the code to meet the requirements of the assignment; I was supposed to return the 
# percentage of rolls that were multiples of 10, but I was returning the number of multiples of 10.	
# The change is in the function count_multiples_of_ten, where I have changed the return value to return the percentage of rolls that were multiples of 10.

import sys, random

#  function to test a parameter for numeric values
def casttoint(argtest): 
	try: 
		holdme = int(argtest)
		return holdme
	except ValueError: 
		print(f'\n\n\t*****ERROR CONDITION*****\n\n\tPlease only enter numberic arguments; you entered {argtest}\n\n')
		sys.exit() 

#  using compression structure to evaluate argv values for ints, and making calls to the function casttoint, to terminate program if 
#  any arg other than the script name [1:], is non-iteger 
[casttoint(args) for args in sys.argv[1:3]]
print(f"\n\tThere were {len(sys.argv)} entered \n")  
#  Check for correct number of parameters. Expect 2: one is the number of die sides, the second in number of rolls.  
#  If len(sys.argv) < 3, , then either only 1 was entered (length = 2) or none were entered (length = 1) 
#  If len(sys.argv) > 3, then too many were entered.  In any of these cases, the execution ends
if len(sys.argv) < 3 or len(sys.argv) >3:
	print("\n\n\t*****ERROR CONDITION*****\n\nThis program requires two inputs: \n  The number of sides on the die \n  The number of rolls")	
	if len(sys.argv) == 1:
		print("\n\tNONE were provided\n")
		sys.exit()
	elif len(sys.argv) == 2:
		print(f"\n\tonly ONE was provided.  Its value is: {sys.argv[1]}\n")
		sys.exit()
	else: 
		print("\n\tTOO MANY were provided\n")
		sys.exit()

sides=int(sys.argv[1])
num_rolls=int(sys.argv[2])

# with all parm presence and int values checked/validated, now determine if the number of sides meet my assumptions on a fair die
if sides not in [2, 4, 6, 8, 12, 20, 100]: 
	print(f"\n\n\t *****INVALID NUMBER OF SIDES - UNFAIR DIE*****\n\n\t Entered: {sides}; must be 2, 4, 6, 8, 12, 20 or 100 sides.")
	sys.exit()

# want to print the input parms in a nifty table like format - notice use of compression to print the two input argumentscast each of the two args into ints in seperate trys.  use function casttoint. if exception, then print msg and execution ends
argnames = ['script name', 'die sides', 'num of rolls']
argvalues = [sys.argv[0], sys.argv[1], sys.argv[2]]
print("\n\n   Parameter line arguments:  ")
print("-" * 30)
# using compression approach from the article- with inline print iterating through args in the sys.argv input, along with formating 
# to produce table
[print(f"{argnames:<18} | {argvalues:>12}") for argnames, argvalues in zip(argnames, argvalues)]

# function to roll the die the num of times in the arguments.  count the num of rolls that are multiples of ten
def count_multiples_of_ten(sides, num_rolls):
	# This rolls the n-sided die, checks if it's a multiple of 10 using modulus 10 - if so, I addd 1 to the total, for the 'num_rolls' 
	count = sum(1 for i in range(num_rolls) if random.randint(1, sides) % 10 == 0) 
	return count

# now call the function with the parms
if sides >=12: 
	total_tens = count_multiples_of_ten(sides, num_rolls)
	print(f"\n\n\tOut of {num_rolls} rolls, a multiple of 10 appeared {total_tens/num_rolls*100:.2f}% of the time.\n\n")
else: 
	print(f"\n\n\tNO tens were rolled, because your die had fewer than 10 sides\n\n")

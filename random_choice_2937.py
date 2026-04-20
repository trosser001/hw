#  PLEASE pardon the excessive indentation - my nano setup is stock, and I haven't taken the time to clean up the tab distance.  There's a lot of indentation as a result, again - my apologies!
import sys 
import re 
import string 
#  Assignment: Write a program that estimates the number of unique words, made only of letters, in the text whose pathname is passed as argument. Test with /users/abrick/resources/urantia.txt

#  Assumptions: I used string.punctuation which is a python string of things used as punctuation: it contains: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ and string.digits which contains: 0123456789
#  my approach was to remove these items, and to convert all words to lower case.  That would eliminate counting capitalized and lower case versions of words for example: "'Joy' is fun day" and "Fun is a day of joy"
#  BUT it does leave Joy out of it, and she's not happy about being uncounted.  
  
#  I also used a set - please check them out - for getting a group of non-repeated things, it is a perfect data structure.  

def unique_words(file_name_and_location): # function to perform cleansing and count of unique words in file passed to the function
    
	unique_words_to_count=set()	# as I used in the unique parm exercise, a set is a datastructure which automagically eliminates any duplicates you might add.
    just_delete_these=string.punctuation + string.digits	# .punctuation and .digits are attributes/constants defined in the "string" library - search them up - powerful.
    remove=str.maketrans('', '',just_delete_these)	#  this uses the native string related class in python3 - 'str', vs the 'string' class I used above
                  	                            	#  maketrans is a "mapping" table - very efficient.  syntax: find (arg1 - '',) and replaces with (arg2 -'',), and arg3 (to_remove) is a string of characters you want to delete. I 
                        	                    	#  don't search for anything to be replaced, I just have it delete what is in my list (just_delete_these)
								   					#  --- it is used by the string ".translate" method to find&replace, and to remove things from strings
	try: 
		with open(file_name_and_location, "r") as file: # "with" is a context manager thing - it manages closing the file if anything goes wrong.
            
			for line in file:
            
				line=line.lower() # make everything lower case
                
				cleanline=line.translate(remove) #  using string predefined things (puncuation marks and numbers, plus my )
                
				list_of_words=cleanline.split() #  uses a string function that separates words...IMPORTANT - gives a LIST of words, which in order to stuff in a SET, you use setname.update(listofwords)
                
				uniques_wordsupdate(list_of_words) #  this 'update' puts each word in the list of words, into the set "unique_words_to_count".  The set magically deletes all duplicates.
                
		return unique_words  #  returns the count of unique cleaned words.
    
	except Exception as e:
				print(f"Problem: Unexpected error with input file occured: {e}")

	return None # Thanks to the "with" context manager, the file will be closed without issue

# USER INSTRUCTIONS: you are welcome to try any file; just enter the address and name of a file and you'll be presented the estimated count of unique words it contains

file_name_and_location = '/users/abrick/resources/urantia.txt' 
num_of_unique_words = count_unique_words(file_name_and_location) 

if num_of_unique_words is not None: 
	print(f"Estimated count of unique words is: {num_of_unique_words} in '{file_name_and_location}'.")


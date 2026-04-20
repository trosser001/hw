import random
import sys 
import re 
import string 
import numpy as np

# assignment: Write a program that shows ten unique random words, made only of letters, and over ten letters long, that occur in the text whose pathname is passed as argument. Test with /users/abrick/resources/urantia.txt 

def unique_words(file_name_and_location): 
    set_unique_words = set() # a set is a data structure that automatically eliminates duplicates
    delete_these = string.punctuation + string.digits  # creates a variable which is a list of punctuation defined by Python geeks, and the set of digits (0-9).  This is a string.  it is used in maketrans
    remove = str.maketrans(delete_these, len(delete_these)*" ") # I finally figured this out: arg1: of maketrans is the search item, arg2: is the replace item. if you use a set of items to search for (delete_these), then the replacement item is actually requeired to be the length of the whole set of charatactes.  So i replace with a string the length of the concatenated punctiuation and digits. 
   
    try: 
        with open(file_name_and_location, "r") as file: 
            for line in file:
                line = line.lower() # converts all letters to lower case
                cleanline = line.translate(remove) # deletes punctuation and digits from the text
                list_of_words = cleanline.split() 
                set_unique_words.update(list_of_words) # adds the list of words to the set
                
        return list(set_unique_words) # returns the SET of unique words, but casts as a list, so it can be used by numpy random.choice
    
    except Exception as e: # Per Prof Bricks instructions, I use a generic exception handler to catch all errors.
        print(f"problem: unexpected error with input file occured: {e}") # if an error occurs, it prints the error and returns None
        return None # python's version of null - it's a placeholder for when an error occurs, and controls the logic in the __main__ block.

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Please provide a file path as an argument.")
        print("Usage: python3 hw_2937.py /path/to/your/file.txt")
        sys.exit(1) # Stops the program gracefully
        
    # Grab the first argument typed after the script name
    file_name_and_location = sys.argv[1]

    #file_name_and_location = '/users/abrick/resources/urantia.txt' 
    long_words = [word for word in unique_words(file_name_and_location) if len(word) > 10] # creates a list of all the unique words in the input file, that are over 10 letters long, using a list compression style loop.
    random_long_words = np.random.choice(long_words, size=10, replace=False)  # 10 random words from the list of unique words - using numpy random.choice; we use it in Math 108 Data Science with Python.  It returns a set of 10 words, from the list of words, and replace = false, is it does not put the word it just chose back into the sample for the next selection.

    if random_long_words is not None: 
        print(f"\nHere are 10 randomly chosen, unique words in '{file_name_and_location}':\n")
        print(f"\n".join(random_long_words),"\n")


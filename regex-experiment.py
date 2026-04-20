import time

text = "energy-carrier"
current_word_buffer = ""
final_matches = []

print(f"Target Text: '{text}'")
print("Pattern: [a-zA-Z]+ (Look for 1 or more consecutive letters)\n")
print("STARTING SCAN...")
print("=" * 40)

# We loop through every single character, just like the regex engine does
for char in text:
    print(f"Examining: '{char}'")
    
    # .isalpha() checks if the character is a letter (a-z, A-Z)
    if char.isalpha():
        current_word_buffer += char
        print(f"  -> It's a letter! Adding to buffer. Current buffer: '{current_word_buffer}'")
    
    # If it's NOT a letter (like our hyphen)
    else:
        print(f"  -> '{char}' is NOT a letter. Pattern broken!")
        
        # If we have letters saved in our buffer, save them as a complete word
        if current_word_buffer:
            final_matches.append(current_word_buffer)
            print(f"  -> SAVED WORD: '{current_word_buffer}' added to final list.")
            current_word_buffer = "" # Clear the buffer to start fresh
            
    time.sleep(0.5) # Pauses for half a second so you can watch it run
    print("-" * 40)

# Once the loop finishes, we check if there's one last word stuck in the buffer
if current_word_buffer:
    final_matches.append(current_word_buffer)
    print(f"End of text! SAVED final word: '{current_word_buffer}'")

print("=" * 40)
print(f"FINAL RESULT LIST: {final_matches}")
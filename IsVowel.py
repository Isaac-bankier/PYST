##############################
#         IsVowel.py         #
# Check if a char is a vowel #
#      By Isaac Bankier      #
##############################

# I tried to teach people a new swear word with no consonants in it...
# Apparently it was vowel language

def IsVowel(char):
    vowels = list("aeiou") # Define all of the vowels

    char = char[0] # Ensure that it is a character not a string.

    if char.lower() in vowels: # Check if the char is a vowel.
        return True

    else:
        return False

print(IsVowel(input("What character do you want to check: ")))

##############################
#        translate.py        #
#       Translate to R       #
#      By Isaac Bankier      #
##############################
 
#TODO add more comments

def IsVowel(char):
    vowels = list("aeiou") # Define all of the vowels

    char = char[0] # Ensure that it is a character not a string.

    if char.lower() in vowels: # Check if the char is a vowel.
        return True

    else:
        return False

def translate(text):
    newString = ""
    for char in text:
        if not IsVowel(char):
            newString += char+"o"+char

    return newString

print(translate(input("What text do you want to translate: ")))

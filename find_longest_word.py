###############################
#         sentence.py         #
# Get the length of each word #
#      By Isaac Bankier       #
###############################

lengths = {}

def longest_word(string):
    words = string.split(" ") #Split the word
    for word in words: #Loop through the words
        lengths[len(word)] = word #add the word length to a dictionary and store the word as its value
    return (lengths[sorted(lengths.keys())[::-1][0]], lengths[sorted(lengths.keys())[::-1][0]]) #sort the lengths of words and return the longest word and its length

print(table("This is a random test string."))

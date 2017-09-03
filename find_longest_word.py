###############################
#         sentence.py         #
# Get the length of each word #
#      By Isaac Bankier       #
###############################

lengths = {}

def table(string):
    words = string.split(" ")
    for word in words:
        lengths[len(word)] = word
    return (lengths[sorted(lengths.keys())[::-1][0]], lengths[sorted(lengths.keys())[::-1][0]])

print(table("This is a random test string."))

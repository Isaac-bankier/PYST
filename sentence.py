###############################
#         sentence.py         #
# Get the length of each word #
#      By Isaac Bankier       #
###############################

#Not sure about the layout of the output so there will be two options.
#TODO strip symbols

def inPlace(string):
    words = string.split(" ")
    newString = ""
    for word in words:
        newString += str(len(word)) + " "
    print(newString)

def table(string):
    words = string.split(" ")
    for word in words:
        print(word + " | " + str(len(word)))

table("This is a random test string")
inPlace("This is a random test string")

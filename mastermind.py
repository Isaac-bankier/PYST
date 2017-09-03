##############################
#        mastermind.py       #
#       Play mastermind      #
#      By Isaac Bankier      #
##############################

import random

class game(object):
    #Set initial attributes
    def __init__(self, length = 4, maxGuesses = 12, chars = ['a', 'b', 'c', 'd', 'e', 'f']):
        self.chars = chars
        self.maxGuesses = maxGuesses
        self.length = length
        self.code = ""
        self.guesses = 0
        self.guessed = False

    #Generate a random code.
    def start(self):
        self.code = ''.join([self.chars[random.randint(0, len(self.chars)-1)] for x in range(0, self.length)])
        return self.code

    #Check if the user can play
    def canPlay(self):
        return (self.guesses < self.maxGuesses) and (self.guessed == False)

    #Allow the user to make a guess
    def guess(self, chars):
        if len(chars) != len(self.code): #Invalid guess
            return

        if chars == self.code: #They win
            self.guessed = True
            return "You win!"

        #temp vars
        tempChars = list(chars)
        tempCode = list(self.code)
        samePlace = 0
        sameType = 0

        #Find if they have any of the guessed characters in the same place and if they have any in the wrong place but the same type.
        for char in range(0, len(tempChars)):
            for testChar in range(0, len(tempCode)):
                if (char == testChar) and (tempChars[char] == tempCode[testChar]):
                    tempCode[testChar] = ''
                    samePlace +=1
                    #Same place
                    break

                if (tempChars[char] == tempCode[testChar]):
                    tempCode[testChar] = ''
                    sameType +=1
                    #Same type
                    break

        self.guesses += 1

        if self.maxGuesses - self.guesses == 0:
            return "You lose!" #They lost

        return "You had "+str(samePlace)+" in the correct place and "+str(sameType)+" of the correct type. You have "+str(self.maxGuesses - self.guesses)+" turns left."

g = game()
g.start()
while g.canPlay():
    print(g.guess(input("Guess: ")))

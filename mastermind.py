##############################
#        mastermind.py       #
#       Play mastermind      #
#      By Isaac Bankier      #
##############################

import random

class game(object):
    def __init__(self, length = 4, maxGuesses = 12, chars = ['a', 'b', 'c', 'd', 'e', 'f']):
        self.chars = chars
        self.maxGuesses = maxGuesses
        self.length = length
        self.code = ""
        self.guesses = 0
        self.guessed = False

    def start(self):
        self.code = ''.join([self.chars[random.randint(0, len(self.chars)-1)] for x in range(0, self.length)])
        return self.code

    def canPlay(self):
        return (self.guesses < self.maxGuesses) and (self.guessed == False)

    def guess(self, chars):
        if len(chars) != len(self.code):
            return

        if chars == self.code:
            self.guessed = True
            return "You win!"

        tempChars = list(chars)
        tempCode = list(self.code)
        samePlace = 0
        sameType = 0

        for char in range(0, len(tempChars)):
            for testChar in range(0, len(tempCode)):
                if (char == testChar) and (tempChars[char] == tempCode[testChar]):
                    tempCode[testChar] = ''
                    samePlace +=1
                    break

                if (tempChars[char] == tempCode[testChar]):
                    tempCode[testChar] = ''
                    sameType +=1
                    break

        self.guesses += 1

        if self.maxGuesses - self.guesses == 0:
            return "You loose!"

        return "You had "+str(samePlace)+" in the correct place and "+str(sameType)+" of the correct type. You have "+str(self.maxGuesses - self.guesses)+" turns left."

g = game()
print(g.start())
while g.canPlay():
    print(g.guess(input("Guess: ")))

##############################
#         hangman.py         #
#           hangman          #
#      By Isaac Bankier      #
##############################

import random

class game(object):
    #Define initial attributes
    def __init__(self, words=["linux", "onion", "github", "firefox", "gimp", "kernal"], guesses=7):
        self.words = words
        self.maxGuesses = guesses
        self.word = ""
        self.guesses = 0
        #Define my great art.
        self.art =\
["","""
    ___
""","""
       |
       |
       |
    ___|
""","""
________
       |
       |
       |
    ___|
""","""
________
      \|
       |
       |
    ___|
""","""
________
|     \|
       |
       |
    ___|
""","""
________
|     \|
O      |
       |
    ___|
""","""
________
|     \|
O      |
X      |
    ___|
"""]

    #Get a random word.
    def start(self):
        self.word = list(random.choice(self.words))
        return self.word

    #Check if the user can play
    def canPlay(self):
        return (self.guesses < self.maxGuesses) and (not (len(self.word) == 0))

    def guess(self, char):
        #See if the character they guessed is in there and remove it
        try:
            self.word.remove(char)
            if len(self.word) == 0:
                return "You win!"
        except ValueError:
            #They are wrong. Show art.
            self.guesses += 1
            if self.guesses == self.maxGuesses:
                return self.art[self.guesses]+"\nGame over!"
            return self.art[self.guesses]+"You have " + str(self.maxGuesses - self.guesses) + " guesses left. "


        return "Correct. You have " + str(self.maxGuesses - self.guesses) + " guesses left. "

g = game()
print(g.start())
while g.canPlay():
    print(g.guess(input("Guess: ")[0]))

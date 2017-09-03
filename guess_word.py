##############################
#        guess_word.py       #
#       Guess the word       #
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

    #Get a random word
    def start(self):
        self.word = list(random.choice(self.words))
        return self.word

    #Check if they can play
    def canPlay(self):
        return (self.guesses < self.maxGuesses) and (not (len(self.word) == 0))

    def guess(self, char):
        try:
            #See if the character they guessed is in there and remove it
            self.word.remove(char)
            if len(self.word) == 0:
                return "You win!"
        except ValueError:
            #They are wrong
            self.guesses += 1
            if self.guesses == self.maxGuesses:
                #They lost
                return "Game over!"
            return "Wrong. You have " + str(self.maxGuesses - self.guesses) + " guesses left. "


        return "Correct. You have " + str(self.maxGuesses - self.guesses) + " guesses left. "

g = game()
print(g.start())
while g.canPlay():
    print(g.guess(input("Guess: ")[0]))

##############################
#        guess_word.py       #
#       Guess the word       #
#      By Isaac Bankier      #
##############################

import random

class game(object):
    def __init__(self):
        self.word = ""
        self.chars = []
        self.guessed = []
        self.guessesLeft = 0
        self.words = ["gnu", "linux", "onion", "kernal", "tux", "git", "github", "curry"]

    def newGame(self):
        self.word = random.choice(words)
        self.chars = list(self.word)
        self.guessed = []
        self.guessesLeft = len(word) * 2

    def guess(self):
        

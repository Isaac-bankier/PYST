###############################
#           bingo.py          #
#          Play bingo         #
#      By Isaac Bankier       #
###############################

import random

class game(object):

    def __init__(self, size=100, initialFill = 0.15, spacer=" ", taken="__"):
        self.width = 1
        self.hight = size
        for i in range(1, int(size/2)):
            j = size / i
            if abs(j - i) < abs(self.width - self.hight):
                self.width = j
                self.hight = i

        self.board = [taken if random.random() < (1.0 - initialFill) else str(y).rjust(2, "0") for y in [x for x in range(0, size)]]

        self.width = int(self.width)
        self.hight = int(self.hight)
        self.size = size
        self.initialFill = initialFill
        self.spacer = spacer
        self.taken = taken

    def printBoard(self):
        boardStr = ""
        for i in range(0, self.size):
            if i % (self.width) == 0:
                boardStr += "\n"
            boardStr += self.board[i]+self.spacer
        return boardStr

    def play(self, number):
        self.board[number]=self.taken

g=game()

userIn = ""

while userIn != "q":
    print(g.printBoard())
    userIn = input("\nEnter the called number or type 'q' to quit: ")
    try:
        g.play(int(userIn))
    except:
        continue
